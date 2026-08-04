import hashlib
import json
from pathlib import Path
import numpy as np
from PIL import Image

hbim_dir = Path(__file__).parent
gsa_dir = hbim_dir / "Grounded-Segment-Anything" / "outputs"

mapping_path = hbim_dir / "mappings" / "mapping_000.json"
rendered_image_path = hbim_dir / "images" / "view_000.png"
mask_npy_path = gsa_dir / "mask.npy"
mask_json_path = gsa_dir / "mask.json"
source_image_json_path = gsa_dir / "source_image.json"


def sha256(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


# Refuse de projeter un masque calcule sur une autre image.
if not source_image_json_path.exists():
    raise RuntimeError(
        "outputs/source_image.json est absent. Relancez grounded_sam_demo.py "
        "sur ../images/view_000.png avant voting.py."
    )

with open(source_image_json_path, "r") as f:
    source_image = json.load(f)

if source_image.get("sha256") != sha256(rendered_image_path):
    raise RuntimeError(
        "Le masque et mapping_000.json ne correspondent pas a la meme image. "
        "Lancez Grounded-SAM avec --input_image ../images/view_000.png."
    )

# Load dico 2D -> 3D
with open(mapping_path, "r") as f:
    pixel_to_point = json.load(f)

# Load 2D mask
mask_2d = np.load(mask_npy_path)

with Image.open(rendered_image_path) as rendered_image:
    expected_shape = (rendered_image.height, rendered_image.width)
if mask_2d.shape != expected_shape:
    raise RuntimeError(
        f"Dimensions incompatibles: masque={mask_2d.shape}, "
        f"rendu={expected_shape}."
    )

# Load mask labels
with open(mask_json_path, "r") as f:
    metadata = json.load(f)

id_to_label = {item["value"]: item["label"] for item in metadata}
id_to_logit = {item["value"]: item.get("logit", 1.0) for item in metadata} # score of trust

# Votes dico
point_votes = {}

for coord_str, point_id in pixel_to_point.items():
    # u = X; v = Y
    u, v = map(int, coord_str.split(","))

    # Check if the pixel is within the mask bounds
    if 0 <= v < mask_2d.shape[0] and 0 <= u < mask_2d.shape[1]:
        label_id = mask_2d[v, u]

        # Ignore background (label_id == 0)
        if label_id != 0:
            label = id_to_label.get(label_id, "unknown")
            logit = id_to_logit.get(label_id, 1.0)

            if point_id not in point_votes:
                point_votes[point_id] = {}

            # Add vote for the label with its logit score
            point_votes[point_id][label] = (
                point_votes[point_id].get(label, 0.0) + logit
            )

# Most represented label
point_labels = {}
for point_id, votes in point_votes.items():
    best_label = max(votes, key=votes.get)
    point_labels[point_id] = best_label

# Save
output_path = hbim_dir / "point_labels_000.json"
with open(output_path, "w") as f:
    json.dump(point_labels, f, indent=4)

print(
    f"{len(point_labels)} points 3D etiquetes. Fichier genere : {output_path}"
)
