import json
from pathlib import Path
import numpy as np
import open3d as o3d

# Paths
hbim_dir = Path(__file__).parent
ply_input_path = hbim_dir / "Paris1_segmented.ply"
labels_json_path = hbim_dir / "point_labels_all.json"
ply_output_path = (
    hbim_dir / "Paris1_segmented.ply"
)

# Different colors for different labels
# Need to adapt based on 3D model
color_palette = {
    "streetlight":   (1.000, 0.839, 0.039),  # Jaune
    "window":        (0.514, 0.220, 0.925),  # Violet
    "tree":          (0.176, 0.776, 0.325),  # Vert
    "table":         (0.984, 0.522, 0.000),  # Orange
    "car":           (0.902, 0.224, 0.275),  # Rouge
    "traffic_light": (1.000, 0.365, 0.635),  # Rose
    "sign":          (0.000, 0.502, 0.502),  # Bleu sarcelle
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
