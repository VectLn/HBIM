import open3d as o3d

dataset = o3d.data.PCDPointCloud()
pcd = o3d.io.read_point_cloud(dataset.path)

# 2. Création du visualiseur
vis = o3d.visualization.Visualizer()
# visible=False masque la fenêtre pendant le rendu (ou visible=True si votre GPU exige une fenêtre active)
vis.create_window(width=640, height=480, visible=False)

# 3. Ajout de la géométrie
vis.add_geometry(pcd)

# 4. Configuration de la caméra (position, lookat, orientation)
ctr = vis.get_view_control()
ctr.set_lookat([0.0, 0.0, 0.0])  # Point ciblé
ctr.set_front([1.0, 1.0, 1.0])   # Direction d'observation (vecteur normal à la caméra)
ctr.set_up([0.0, 0.0, 1.0])      # Vecteur vertical (axe Z vers le haut)
ctr.set_zoom(0.8)

# 5. Mise à jour et rendu
vis.poll_events()
vis.update_renderer()

# 6. Capture et sauvegarde de l'image
vis.capture_screen_image("view_001.png", do_render=True)
vis.destroy_window()

print("Rendu sauvegarde sous 'view_001.png'")