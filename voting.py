import hashlib
import json
from collections import Counter
from pathlib import Path

import numpy as np
from PIL import Image


hbim_dir = Path(__file__).parent
images_dir = hbim_dir / "images"
mappings_dir = hbim_dir / "mappings"
gsa_outputs_dir = hbim_dir / "Grounded-Segment-Anything" / "outputs"
output_path = hbim_dir / "point_labels.json"
vote_details_path = hbim_dir / "point_votes.json"


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def view_paths(mapping_path):
    view_id = mapping_path.stem.removeprefix("mapping_")
    view_name = f"view_{view_id}"
    output_dir = gsa_outputs_dir / view_name
    return {
        "name": view_name,
        "image": images_dir / f"{view_name}.png",
        "mask": output_dir / "mask.npy",
        "metadata": output_dir / "mask.json",
        "source": output_dir / "source_image.json",
    }


def validate_view(paths):
    required = [paths["image"], paths["mask"], paths["metadata"], paths["source"]]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise RuntimeError(
            f"Sorties absentes pour {paths['name']}: {', '.join(missing)}. "
            "Executez grounded_sam_batch.py avant voting.py."
        )

    with open(paths["source"], "r") as f:
        source = json.load(f)
    if source.get("sha256") != sha256(paths["image"]):
        raise RuntimeError(
            f"Le masque de {paths['name']} ne correspond plus a son rendu. "
            "Relancez grounded_sam_batch.py."
        )


mapping_paths = sorted(mappings_dir.glob("mapping_*.json"))
if not mapping_paths:
    raise RuntimeError("Aucun mapping trouve. Executez d'abord 2DRenderer.py.")

point_votes = {}
view_summaries = []
legacy_mapping_detected = False

for mapping_path in mapping_paths:
    paths = view_paths(mapping_path)
    validate_view(paths)

    with open(mapping_path, "r") as f:
        pixel_to_point = json.load(f)
    mask_2d = np.load(paths["mask"])
    with open(paths["metadata"], "r") as f:
        metadata = json.load(f)

    with Image.open(paths["image"]) as rendered_image:
        expected_shape = (rendered_image.height, rendered_image.width)
    if mask_2d.shape != expected_shape:
        raise RuntimeError(
            f"Dimensions incompatibles pour {paths['name']}: "
            f"masque={mask_2d.shape}, rendu={expected_shape}."
        )

    id_to_label = {int(item["value"]): item["label"] for item in metadata}
    id_to_logit = {
        int(item["value"]): float(item.get("logit", 1.0)) for item in metadata
    }
    labeled_in_view = 0
    labels_in_view = Counter()

    for coord_str, mapping_value in pixel_to_point.items():
        u, v = map(int, coord_str.split(","))
        if not (0 <= v < mask_2d.shape[0] and 0 <= u < mask_2d.shape[1]):
            continue

        label_id = int(mask_2d[v, u])
        if label_id == 0:
            continue

        if isinstance(mapping_value, dict):
            point_id = int(mapping_value["pt_idx"])
            camera_distance = float(
                mapping_value.get("camera_distance", mapping_value["depth"])
            )
        else:
            # Compatibilite avec les anciens mappings, non ponderes en distance.
            point_id = int(mapping_value)
            camera_distance = 1.0
            legacy_mapping_detected = True

        label = id_to_label.get(label_id, "unknown")
        confidence = id_to_logit.get(label_id, 1.0)
        weight = confidence / max(camera_distance, 1e-12)

        votes = point_votes.setdefault(point_id, {})
        votes[label] = votes.get(label, 0.0) + weight
        labeled_in_view += 1
        labels_in_view[label] += 1

    view_summaries.append((paths["name"], labeled_in_view, labels_in_view))

point_labels = {
    str(point_id): max(votes, key=votes.get)
    for point_id, votes in point_votes.items()
}
serializable_votes = {
    str(point_id): votes for point_id, votes in point_votes.items()
}

with open(output_path, "w") as f:
    json.dump(point_labels, f, indent=4)
with open(vote_details_path, "w") as f:
    json.dump(serializable_votes, f, indent=4)

for view_name, count, labels in view_summaries:
    print(f"{view_name}: {count} projections etiquetees, {dict(labels)}")
if legacy_mapping_detected:
    print(
        "ATTENTION: anciens mappings detectes; relancez 2DRenderer.py pour "
        "activer la ponderation par distance camera."
    )
print(
    f"{len(point_labels)} points 3D etiquetes apres vote sur "
    f"{len(mapping_paths)} vues. Fichier genere : {output_path}"
)
