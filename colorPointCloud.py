import json
from pathlib import Path
import numpy as np
import open3d as o3d

# Paths
hbim_dir = Path(__file__).parent
ply_input_path = hbim_dir / "Maison_Villa.ply"
labels_json_path = hbim_dir / "point_labels_all.json"
ply_output_path = (
    hbim_dir / "Maison_Villa_segmented.ply"
)

# Different colors for different labels
# Need to adapt based on 3D model
color_palette = {
    "house": [0.8, 0.7, 0.6],       # Beige / Tan
    "tree": [0.1, 0.4, 0.15],       # Vert foncé
    "window": [0.0, 0.6, 0.9],      # Bleu ciel
    "pool": [0.0, 0.8, 0.9],        # Bleu piscine / Turquoise
    "car": [0.9, 0.2, 0.2],         # Rouge
    "road": [0.2, 0.2, 0.2],        # Gris foncé
    "grass": [0.4, 0.8, 0.2],       # Vert clair
    "table": [0.55, 0.35, 0.15],    # Marron bois
    "bush": [0.2, 0.6, 0.2],        # Vert moyen
}
default_color = [0.2, 0.2, 0.2] 

# Loading data
pcd = o3d.io.read_point_cloud(str(ply_input_path))
with open(labels_json_path, "r") as f:
    point_labels = json.load(f)

# Give colors to points based on their labels
num_points = len(pcd.points)
colors = np.tile(default_color, (num_points, 1))

for point_idx_str, label in point_labels.items():
    idx = int(point_idx_str)
    if 0 <= idx < num_points:
        colors[idx] = color_palette.get(label, default_color)

# Apply save and show
pcd.colors = o3d.utility.Vector3dVector(colors)
o3d.io.write_point_cloud(str(ply_output_path), pcd)

print(f"Fichier généré : {ply_output_path}")
o3d.visualization.draw_geometries([pcd])
