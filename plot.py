    
def add_polygon_patch_to_image(image, xy_coords):
		
		fig, ax = plt.subplots()
    ax.imshow(image)
    patch = matplotlib.patches.Polygon(xy_coords, closed=True, alpha=0.5, color='red')
    ax.add_patch(patch)
    
    plt.show()