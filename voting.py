import json
from pathlib import Path
import numpy as np

hbim_dir = Path(__file__).parent
mappings_dir = hbim_dir / "mappings"
masks_dir = hbim_dir / "masks"
output_path = hbim_dir / "point_labels_all.json"

# Dictionnaire global des votes
point_votes = {}

# Récupération de tous les fichiers de mapping
mapping_files = sorted(list(mappings_dir.glob("mapping_*.json")))

for mapping_file in mapping_files:
    # Extraction de l'identifiant de vue (ex: mapping_000.json -> view_000)
    view_id = mapping_file.stem.replace("mapping_", "view_")

    mask_npy_path = masks_dir / f"mask_{view_id}.npy"
    mask_json_path = masks_dir / f"mask_{view_id}.json"

    # Vérification de l'existence du masque pour cette vue
    if not mask_npy_path.exists() or not mask_json_path.exists():
        print(f"Masque non trouvé pour {view_id}, vue ignorée.")
        continue

    # Chargement du dico 2D -> 3D
    with open(mapping_file, "r") as f:
        pixel_to_point = json.load(f)

    # Chargement du masque 2D et des métadonnées
    mask_2d = np.load(mask_npy_path)
    with open(mask_json_path, "r") as f:
        metadata = json.load(f)

    id_to_label = {item["value"]: item["label"] for item in metadata}
    id_to_logit = {item["value"]: item.get("logit", 1.0) for item in metadata}

    # Accumulation des votes pour cette vue
    for coord_str, point_id in pixel_to_point.items():
        u, v = map(int, coord_str.split(","))

        if 0 <= v < mask_2d.shape[0] and 0 <= u < mask_2d.shape[1]:
            label_id = mask_2d[v, u]

            # Ignorer le background (label_id == 0)
            if label_id != 0:
                label = id_to_label.get(label_id, "unknown")
                logit = id_to_logit.get(label_id, 1.0)

                if point_id not in point_votes:
                    point_votes[point_id] = {}

                point_votes[point_id][label] = (
                    point_votes[point_id].get(label, 0.0) + logit
                )

# Élection du label majoritaire par point
point_labels = {}
for point_id, votes in point_votes.items():
    best_label = max(votes, key=votes.get)
    point_labels[point_id] = best_label

# Sauvegarde globale
with open(output_path, "w") as f:
    json.dump(point_labels, f, indent=4)

print(
    f"{len(point_labels)} points 3D étiquetés cumulés sur les vues traitées. Fichier généré : {output_path}"
)