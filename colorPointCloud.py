import json
from pathlib import Path
import numpy as np
import open3d as o3d

# 1. Configuration des chemins
hbim_dir = Path(__file__).parent
ply_input_path = hbim_dir / "PointCloud_Lighthouse_MorrisIsland.ply"
labels_json_path = hbim_dir / "point_labels.json"
ply_output_path = (
    hbim_dir / "PointCloud_Lighthouse_MorrisIsland_segmented.ply"
)

# 2. Palette de couleurs RGB (valeurs entre 0.0 et 1.0)
color_palette = {
    "lighthouse": [1.0, 0.0, 0.0],  # Rouge
    "window": [0.0, 0.0, 1.0],  # Bleu
    "door": [0.0, 1.0, 0.0],  # Vert
    "roof": [1.0, 0.5, 0.0],  # Orange
    "wall": [0.8, 0.8, 0.8],  # Gris clair
}
default_color = [0.2, 0.2, 0.2]  # Gris foncé pour les points non étiquetés

# 3. Chargement des données
pcd = o3d.io.read_point_cloud(str(ply_input_path))
with open(labels_json_path, "r") as f:
    point_labels = json.load(f)

# 4. Attribution des couleurs aux points 3D
num_points = len(pcd.points)
colors = np.tile(default_color, (num_points, 1))

for point_idx_str, label in point_labels.items():
    idx = int(point_idx_str)
    if 0 <= idx < num_points:
        colors[idx] = color_palette.get(label, default_color)

# 5. Application, enregistrement et affichage
pcd.colors = o3d.utility.Vector3dVector(colors)
o3d.io.write_point_cloud(str(ply_output_path), pcd)

print(f"Fichier généré : {ply_output_path}")
o3d.visualization.draw_geometries([pcd])
