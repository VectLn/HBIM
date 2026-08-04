import os
import open3d as o3d
import numpy as np
import json
# See https://www.open3d.org/docs/release/index.html

def generate_trajectory_and_mapping(pcd_path="Paris5.ply", num_views=8, width=1280,
                                    height=960, zoom=5, cam_height_multiplier=-0.22, 
                                    lookat_z_offset=-0.4):
    pcd = o3d.io.read_point_cloud(pcd_path)

    # Data given by open3D
    #dataset = o3d.data.PCDPointCloud()
    #pcd = o3d.io.read_point_cloud(dataset.path)

    # Create folder
    img_dir = "images"
    json_dir = "mappings"
    os.makedirs(img_dir, exist_ok=True)
    os.makedirs(json_dir, exist_ok=True)

    points = np.asarray(pcd.points)

    # Bounding box
    bbox = pcd.get_axis_aligned_bounding_box()

    # Center of bounding box
    center = bbox.get_center()
    radius = np.linalg.norm(bbox.get_half_extent())

    vis = o3d.visualization.Visualizer()
    vis.create_window(width=width, height=height, visible=False)
    vis.add_geometry(pcd)

    cam_distance = radius / zoom
    
    for i in range(num_views):
        print(f"Image numero {i}")
        # Compute camera position all around bounding box center
        angle = i * (2 * np.pi / num_views)
        cam_x = center[0] + cam_distance * np.cos(angle)
        cam_y = center[1] + cam_distance * np.sin(angle)
        cam_z = center[2] + (cam_distance * cam_height_multiplier) # Elevate camera for birds eye view
    
        
        # # ---- Control the view of the vizualiser ie extrinsic cam parameters [R|t] ----
        # # https://towardsdatascience.com/what-are-intrinsic-and-extrinsic-camera-parameters-in-computer-vision-7071b72fb8ec/
        # ctr = vis.get_view_control()
        # # Lookat
        # ctr.set_lookat(center)
        # # Vector pointing FROM lookat TO camera (cam_pos - lookat)
        # ctr.set_front([cam_x - center[0], cam_y - center[1], cam_z - center[2]])
        # # Z axis
        # ctr.set_up([0, 0, 1])

        # Constructs extrinsic matrix manually
        cam_pos = np.array([cam_x, cam_y, cam_z])
        lookat = np.array([center[0], center[1], center[2] + cam_distance * lookat_z_offset])
        up = np.array([0, 0, 1])

        # 1. Z_cam points FORWARD (from camera to lookat)
        z_cam = lookat - cam_pos
        z_cam = z_cam / np.linalg.norm(z_cam)

        # 2. X_cam points RIGHT
        x_cam = np.cross(z_cam, up)
        x_cam = x_cam / np.linalg.norm(x_cam)

        # 3. Y_cam points DOWN
        y_cam = np.cross(z_cam, x_cam)

        R = np.vstack([x_cam, y_cam, z_cam])
        t = -R @ cam_pos

        extrinsic_matrix = np.eye(4)
        extrinsic_matrix[:3, :3] = R
        extrinsic_matrix[:3, 3] = t

        # Apply extrinsic directly to vizualiser
        ctr = vis.get_view_control()
        cam_params = ctr.convert_to_pinhole_camera_parameters()
        cam_params.extrinsic = extrinsic_matrix
        ctr.convert_from_pinhole_camera_parameters(cam_params, True)

        # Render
        vis.poll_events()
        vis.update_renderer()
        
        # Save image
        img_name = os.path.join(img_dir, f"view_{i:03d}.png")
        vis.capture_screen_image(img_name, do_render=True)
        
        # Get extrinsic and intrinsic matrix of cam parameters
        cam_params = ctr.convert_to_pinhole_camera_parameters()
        extrinsic = np.copy(cam_params.extrinsic) # Matrix [R|t] 4x4
        intrinsic = cam_params.intrinsic.intrinsic_matrix # Matrix K 3x3
        
        # ---- 3D -> 2D ----
        # Homogeneous coordinates (X, Y, Z, 1) ie cartesian coordinates scaled
        points_homo = np.hstack((points, np.ones((points.shape[0], 1))))
        
        # Convert global coordinates to cam coordinates ([R|t].x_world)
        points_cam = (extrinsic @ points_homo.T).T
        
        # Filters out points behind camera
        valid_points = points_cam[:, 2] > 0 # Z is 3rd row, if Z < 0 then the point is behind the camera
        points_cam_valid = points_cam[valid_points]
        
        # Projects on image plan (K.points_cam)
        # ps Information on image definition is in K
        points_2d_homo = (intrinsic @ points_cam_valid[:, :3].T).T
        u = (points_2d_homo[:, 0] / points_2d_homo[:, 2]).astype(int) # Division by w to account for perspective
        v = (points_2d_homo[:, 1] / points_2d_homo[:, 2]).astype(int)
        depth = points_cam_valid[:, 2]
        
        # index from point cloud
        original_idx = np.where(valid_points)[0]
        
        # Filters out points outside the image
        in_image = (u >= 0) & (u < width) & (v >= 0) & (v < height)
        u = u[in_image]
        v = v[in_image]
        depth = depth[in_image]
        original_idx = original_idx[in_image]
        
        # Z Buffer occlusion
        mapping = {}
        for idx in range(len(u)):
            # Key is u,v in json
            pixel_key = f"{u[idx]},{v[idx]}"
            d = depth[idx]
            pt_idx = int(original_idx[idx])
            
            # Only keep closest point to camera
            if pixel_key not in mapping or d < mapping[pixel_key]['depth']:
                mapping[pixel_key] = {'pt_idx': pt_idx, 'depth': float(d)}
        
        # Only keep idx and depth
        final_mapping = { k: {"pt_idx": v["pt_idx"], "depth": v["depth"]} for k, v in mapping.items()}
        
        # Save dico
        dict_name = os.path.join(json_dir, f"mapping_{i:03d}.json")
        with open(dict_name, 'w') as f:
            json.dump(final_mapping, f)

    vis.destroy_window()

# Execute
generate_trajectory_and_mapping()