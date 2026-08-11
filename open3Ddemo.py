import argparse

import numpy as np
import open3d as o3d


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path")
    args = parser.parse_args()

    pcd = o3d.io.read_point_cloud(args.input_path)
    if not pcd.has_colors():
        raise ValueError(
            "Ce PLY ne contient pas de couleurs RGB standard. "
            "Convertissez-le d'abord avec GaussianToRGB.py."
        )

    vis = o3d.visualization.VisualizerWithKeyCallback()
    vis.create_window(window_name="Visualisation Open3D")
    vis.add_geometry(pcd)

    step_move = 0.2
    step_rot = np.radians(5)

    def update_camera(dx=0.0, dy=0.0, dz=0.0, rx=0.0, ry=0.0, rz=0.0):
        view_ctl = vis.get_view_control()
        params = view_ctl.convert_to_pinhole_camera_parameters()
        ext = params.extrinsic

        # Deplacement dans le repere local de la camera.
        translation = np.eye(4)
        translation[0, 3] = dx
        translation[1, 3] = dy
        translation[2, 3] = dz

        # Rotation verticale autour de l'axe X local (pitch).
        rotation_x = np.eye(4)
        if rx != 0:
            rotation_x[1, 1] = np.cos(rx)
            rotation_x[1, 2] = -np.sin(rx)
            rotation_x[2, 1] = np.sin(rx)
            rotation_x[2, 2] = np.cos(rx)

        # Rotation horizontale autour de l'axe Y local (yaw).
        rotation_y = np.eye(4)
        if ry != 0:
            rotation_y[0, 0] = np.cos(ry)
            rotation_y[0, 2] = np.sin(ry)
            rotation_y[2, 0] = -np.sin(ry)
            rotation_y[2, 2] = np.cos(ry)

        # Ancienne rotation Z/X autour de l'axe Z local.
        rotation_z = np.eye(4)
        if rz != 0:
            rotation_z[0, 0] = np.cos(rz)
            rotation_z[0, 1] = -np.sin(rz)
            rotation_z[1, 0] = np.sin(rz)
            rotation_z[1, 1] = np.cos(rz)

        params.extrinsic = rotation_x @ rotation_y @ rotation_z @ translation @ ext
        view_ctl.convert_from_pinhole_camera_parameters(params, True)
        return False

    # W/S : avancer / reculer.
    vis.register_key_callback(ord("W"), lambda v: update_camera(dz=-4 * step_move))
    vis.register_key_callback(ord("S"), lambda v: update_camera(dz=4 * step_move))

    # A/D : gauche / droite.
    vis.register_key_callback(ord("A"), lambda v: update_camera(dx=4 * step_move))
    vis.register_key_callback(ord("D"), lambda v: update_camera(dx=-4 * step_move))

    # Q/E : descendre / monter.
    vis.register_key_callback(ord("Q"), lambda v: update_camera(dy=-4 * step_move))
    vis.register_key_callback(ord("E"), lambda v: update_camera(dy=4 * step_move))

    # Conserver les anciennes touches Z/X de rotation.
    vis.register_key_callback(ord("Z"), lambda v: update_camera(rz=-step_rot / 5))
    vis.register_key_callback(ord("X"), lambda v: update_camera(rz=step_rot / 5))

    # Codes GLFW des fleches du clavier.
    key_right = 262
    key_left = 263
    key_down = 264
    key_up = 265

    # Fleches gauche/droite : tourner la camera horizontalement.
    vis.register_key_callback(key_left, lambda v: update_camera(ry=step_rot / 5))
    vis.register_key_callback(key_right, lambda v: update_camera(ry=-step_rot / 5))

    # Fleches haut/bas : regarder vers le haut ou vers le bas.
    vis.register_key_callback(key_up, lambda v: update_camera(rx=-step_rot / 5))
    vis.register_key_callback(key_down, lambda v: update_camera(rx=step_rot / 5))

    vis.run()
    vis.destroy_window()


if __name__ == "__main__":
    main()
