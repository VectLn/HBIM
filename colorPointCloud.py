import json
from pathlib import Path
import numpy as np
import open3d as o3d

# Paths
hbim_dir = Path(__file__).parent
ply_input_path = hbim_dir / "Villa.ply"
labels_json_path = hbim_dir / "point_labels_all.json"
ply_output_path = (
    hbim_dir / "Villa_segmented.ply"
)

# Different colors for different labels
# Need to adapt based on 3D model
color_palette = {
    "house":         (0.820, 0.700, 0.500),  # Beige pierre
    "road":          (0.220, 0.220, 0.220),  # Gris asphalte
    "grass":         (0.350, 0.700, 0.200),  # Vert herbe
    "window":        (0.300, 0.700, 0.900),  # Bleu ciel
    "car":           (0.850, 0.120, 0.100),  # Rouge automobile
    "tree":          (0.100, 0.500, 0.150),  # Vert feuillage foncé
    "pool": (0.000, 0.700, 0.900),  # Bleu aquatique
    "fence":         (0.450, 0.300, 0.180),  # Marron bois
    "table":         (0.650, 0.400, 0.200),  # Marron clair
    "bush":          (0.200, 0.600, 0.250),  # Vert buisson
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
