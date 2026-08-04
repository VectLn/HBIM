import json
from pathlib import Path
import numpy as np

hbim_dir = Path(__file__).parent
mappings_dir = hbim_dir / "mappings"
masks_dir = hbim_dir / "masks"
output_path = hbim_dir / "point_labels_all.json"

# Global dictionary to accumulate votes for each 3D point
point_votes = {}

# Every mapping file
mapping_files = sorted(list(mappings_dir.glob("mapping_*.json")))

for mapping_file in mapping_files:
    # Extract id
    view_id = mapping_file.stem.replace("mapping_", "view_")

    mask_npy_path = masks_dir / f"mask_{view_id}.npy"
    mask_json_path = masks_dir / f"mask_{view_id}.json"

    # Is there a mask for this view
    if not mask_npy_path.exists() or not mask_json_path.exists():
        print(f"Masque non trouvé pour {view_id}, vue ignorée.")
        continue

    # Loading dico 2D -> 3D
    with open(mapping_file, "r") as f:
        pixel_to_point = json.load(f)

    # Loading mask and metadata
    mask_2d = np.load(mask_npy_path)
    with open(mask_json_path, "r") as f:
        metadata = json.load(f)

    id_to_label = {item["value"]: item["label"] for item in metadata}
    id_to_logit = {item["value"]: item.get("logit", 1.0) for item in metadata}

    # Accumulate votes for each 3D point based on the 2D mask and mapping
    for coord_str, point_data in pixel_to_point.items():
        u, v = map(int, coord_str.split(","))

        # Extract point_id and depth from point_data
        if isinstance(point_data, dict):
            point_id = point_data["pt_idx"]
            d_cam = point_data["depth"]
        else:
            point_id = point_data
            d_cam = 1.0  # If depth is not provided

        if 0 <= v < mask_2d.shape[0] and 0 <= u < mask_2d.shape[1]:
            label_id = mask_2d[v, u]

            if label_id != 0:
                label = id_to_label.get(label_id, "unknown")
                logit = id_to_logit.get(label_id, 1.0)

                # weight = logit / d_cam
                weight = logit / max(d_cam, 1e-5)

                if point_id not in point_votes:
                    point_votes[point_id] = {}

                point_votes[point_id][label] = (
                    point_votes[point_id].get(label, 0.0) + weight
                )

# Voting for majority label for each 3D point
point_labels = {}
for point_id, votes in point_votes.items():
    best_label = max(votes, key=votes.get)
    point_labels[point_id] = best_label

# Save
with open(output_path, "w") as f:
    json.dump(point_labels, f, indent=4)

print(
    f"{len(point_labels)} points 3D étiquetés cumulés sur les vues traitées. Fichier généré : {output_path}"
)