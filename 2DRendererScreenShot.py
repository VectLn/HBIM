import argparse
import json
import re
import shutil
from pathlib import Path
import numpy as np
import open3d as o3d


def get_next_view_index(img_dir, map_dir):
    """Trouve le premier indice disponible pour ne pas écraser l'existant."""
    existing_indices = []

    # Recherche des indices existants dans le dossier des images
    for file in img_dir.glob("view_*.png"):
        match = re.search(r"view_(\d+)\.png", file.name)
        if match:
            existing_indices.append(int(match.group(1)))

    # Recherche des indices existants dans le dossier des dicos
    for file in map_dir.glob("mapping_*.json"):
        match = re.search(r"mapping_(?:view_)?(\d+)\.json", file.name)
        if match:
            existing_indices.append(int(match.group(1)))

    return max(existing_indices) + 1 if existing_indices else 0


def generate_mapping(points, cam_params):
    """Génère le dictionnaire de mapping Z-buffer."""
    extrinsic = cam_params.extrinsic
    intrinsic = cam_params.intrinsic.intrinsic_matrix
    width = cam_params.intrinsic.width
    height = cam_params.intrinsic.height

    points_homo = np.hstack((points, np.ones((points.shape[0], 1))))
    points_cam = (extrinsic @ points_homo.T).T

    valid_points = points_cam[:, 2] > 0
    points_cam_valid = points_cam[valid_points]
    original_idx = np.where(valid_points)[0]

    points_2d_homo = (intrinsic @ points_cam_valid[:, :3].T).T
    u = (points_2d_homo[:, 0] / points_2d_homo[:, 2]).astype(int)
    v = (points_2d_homo[:, 1] / points_2d_homo[:, 2]).astype(int)
    depth = points_cam_valid[:, 2]

    in_image = (u >= 0) & (u < width) & (v >= 0) & (v < height)
    u = u[in_image]
    v = v[in_image]
    depth = depth[in_image]
    original_idx = original_idx[in_image]

    mapping = {}
    for idx in range(len(u)):
        pixel_key = f"{u[idx]},{v[idx]}"
        d = float(depth[idx])
        pt_idx = int(original_idx[idx])

        if pixel_key not in mapping or d < mapping[pixel_key]["depth"]:
            mapping[pixel_key] = {"pt_idx": pt_idx, "depth": d}

    return mapping


def process_user_screenshots(ply_path, img_dir="images", map_dir="mappings"):
    img_path = Path(img_dir)
    map_path = Path(map_dir)
    img_path.mkdir(parents=True, exist_ok=True)
    map_path.mkdir(parents=True, exist_ok=True)

    pcd = o3d.io.read_point_cloud(ply_path)
    points = np.asarray(pcd.points)

    current_idx = get_next_view_index(img_path, map_path)

    # Recherche des paires ScreenCamera_*.json
    camera_json_files = list(Path(".").glob("ScreenCamera_*.json"))
    processed_count = 0

    for json_file in camera_json_files:
        # Extraction de l'horodatage pour cibler l'image correspondante
        timestamp = json_file.name.replace("ScreenCamera_", "").replace(
            ".json", ""
        )
        img_file = Path(f"ScreenCapture_{timestamp}.png")

        if not img_file.exists():
            print(
                f"Image introuvable pour {json_file.name} (attendu : {img_file.name}), fichier ignoré."
            )
            continue

        try:
            cam_params = o3d.io.read_pinhole_camera_parameters(str(json_file))
        except Exception as e:
            print(f"Erreur de lecture sur {json_file.name} : {e}")
            continue

        new_img_name = f"view_{current_idx:03d}.png"
        new_map_name = f"mapping_{current_idx:03d}.json"

        # Calcul du dictionnaire et écriture
        mapping = generate_mapping(points, cam_params)
        with open(map_path / new_map_name, "w") as f:
            json.dump(mapping, f)

        # Copie de l'image
        shutil.copy(img_file, img_path / new_img_name)

        print(
            f"Ajouté [{current_idx:03d}] : {img_file.name} -> {img_dir}/{new_img_name} et {map_dir}/{new_map_name}"
        )

        current_idx += 1
        processed_count += 1

    print(f"Terminé : {processed_count} capture(s) intégrée(s).")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Intègre les captures ScreenCapture/ScreenCamera dans le dataset sans écraser l'existant."
    )
    parser.add_argument("ply_path", help="Chemin du fichier .ply source")
    parser.add_argument(
        "--img_dir", default="images", help="Dossier cible des images"
    )
    parser.add_argument(
        "--map_dir", default="mappings", help="Dossier cible des dicos"
    )
    args = parser.parse_args()

    process_user_screenshots(args.ply_path, args.img_dir, args.map_dir)