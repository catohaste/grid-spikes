    
def add_polygon_patch_to_image(image, xy_coords):
    
    # brightfield_im = skio.imread(data_folder + image.name + "/" + image.prefix + " brightfield" + image.suffix, plugin="tifffile")
		
	fig, ax = plt.subplots()
    ax.imshow(image)
    patch = matplotlib.patches.Polygon(xy_coords, closed=True, alpha=0.5, color='red')
    ax.add_patch(patch)
    
    plt.show()
    
def plot_brightfield_with_grid(data_folder, image, xy_coords):
    
    # brightfield_im = skio.imread(data_folder + image.name + "/" + image.prefix + " brightfield" + image.suffix, plugin="tifffile")
		
	fig, ax = plt.subplots()
    ax.imshow(image)
    patch = matplotlib.patches.Polygon(xy_coords, closed=True, alpha=0.5, color='red')
    ax.add_patch(patch)
    
    plt.show()