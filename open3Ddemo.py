import argparse
import open3d as o3d


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path")
    parser.add_argument("-o", "--output", default="output.ply")
    args = parser.parse_args()

    pcd = o3d.io.read_point_cloud(args.input_path)
    o3d.io.write_point_cloud(args.output, pcd, write_ascii=True)
    o3d.visualization.draw_geometries([pcd], window_name="Visualisation Open3D")


if __name__ == "__main__":
    main()