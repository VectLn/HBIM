import argparse
import numpy as np
import open3d as o3d
from plyfile import PlyData


def convert_3dgs_to_standard_ply(input_path, output_path):
    plydata = PlyData.read(input_path)
    vertex = plydata["vertex"]

    # Coordonnées 3D
    xyz = np.vstack([vertex["x"], vertex["y"], vertex["z"]]).T
    property_names = [p.name for p in vertex.properties]

    # Conversion de la couleur
    if "f_dc_0" in property_names:
        f_dc = np.vstack(
            [vertex["f_dc_0"], vertex["f_dc_1"], vertex["f_dc_2"]]
        ).T
        SH_C0 = 0.28209479177387814
        colors = 0.5 + SH_C0 * f_dc
        colors = np.clip(colors, 0.0, 1.0)
    elif "red" in property_names:
        print("Le fichier contient déjà des canaux RGB standard.")
        r, g, b = vertex["red"], vertex["green"], vertex["blue"]
        colors = np.vstack([r, g, b]).T
        if colors.max() > 1.0:
            colors = colors / 255.0
    else:
        print(
            "Aucune donnée de couleur détectée, attribution d'une couleur grise par défaut."
        )
        colors = np.ones_like(xyz) * 0.5

    # Création du nuage de points Open3D
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(xyz)
    pcd.colors = o3d.utility.Vector3dVector(colors)

    # Correction de l'orientation (remet le nuage à l'endroit)
    R = pcd.get_rotation_matrix_from_xyz((-np.pi / 2, 0, 0))
    pcd.rotate(R, center=pcd.get_center())

    # Sauvegarde au format PLY standard (binaire par défaut)
    o3d.io.write_point_cloud(output_path, pcd)
    print(f"Fichier converti avec succès : {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Convertit un fichier PLY 3D Gaussian Splattering en PLY RGB standard."
    )
    parser.add_argument("input_path", help="Chemin du fichier .ply source (3DGS)")
    parser.add_argument(
        "-o",
        "--output",
        default="standard_output.ply",
        help="Chemin du fichier .ply de sortie",
    )
    args = parser.parse_args()

    convert_3dgs_to_standard_ply(args.input_path, args.output)


if __name__ == "__main__":
    main()