#cd C:\dev\open3D
import open3d as o3d

dataset = o3d.data.PCDPointCloud()
pcd = o3d.io.read_point_cloud("Paris5.ply")

o3d.io.write_point_cloud("output.ply", pcd, write_ascii=True)

o3d.visualization.draw_geometries([pcd], window_name="Visualisation Open3D")