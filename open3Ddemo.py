import argparse
import numpy as np
import open3d as o3d


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path")
    parser.add_argument("-o", "--output", default="output.ply")
    args = parser.parse_args()

    pcd = o3d.io.read_point_cloud(args.input_path)
    o3d.io.write_point_cloud(args.output, pcd, write_ascii=True)

    vis = o3d.visualization.VisualizerWithKeyCallback()
    vis.create_window(window_name="Visualisation Open3D")
    vis.add_geometry(pcd)

    step_move = 0.2
    step_rot = np.radians(5)

    def update_camera(dx=0.0, dy=0.0, dz=0.0, rz=0.0):
        view_ctl = vis.get_view_control()
        params = view_ctl.convert_to_pinhole_camera_parameters()
        ext = params.extrinsic

        # Déplacement dans le repère local de la caméra
        T = np.eye(4)
        T[0, 3] = dx
        T[1, 3] = dy
        T[2, 3] = dz

        # Rotation autour de l'axe Z local (Yaw)
        R = np.eye(4)
        if rz != 0:
            R[0, 0] = np.cos(rz)
            R[0, 1] = -np.sin(rz)
            R[1, 0] = np.sin(rz)
            R[1, 1] = np.cos(rz)

        params.extrinsic = R @ T @ ext
        view_ctl.convert_from_pinhole_camera_parameters(params)
        return False

    # Z/S : Avancer / Reculer
    vis.register_key_callback(ord("W"), lambda v: update_camera(dz=-4*step_move))
    vis.register_key_callback(ord("S"), lambda v: update_camera(dz=4*step_move))

    # Q/D : Gauche / Droite
    vis.register_key_callback(ord("A"), lambda v: update_camera(dx=4*step_move))
    vis.register_key_callback(ord("D"), lambda v: update_camera(dx=-4*step_move))

    # A/E : Élévation (Bas / Haut)
    vis.register_key_callback(ord("Q"), lambda v: update_camera(dy=-4*step_move))
    vis.register_key_callback(ord("E"), lambda v: update_camera(dy=4*step_move))

    # W/X : Rotation (Inclinaison vers le haut / bas)
    vis.register_key_callback(ord("Z"), lambda v: update_camera(rz=-step_rot/5))
    vis.register_key_callback(ord("X"), lambda v: update_camera(rz=step_rot/5))

    vis.run()
    vis.destroy_window()


if __name__ == "__main__":
    main()