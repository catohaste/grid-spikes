import matplotlib.pyplot as plt
import skimage.io as skio

def add_polygon_patch_to_image(image, xy_coords):
    
    brightfield_im = skio.imread(data_folder + image.name + "/" + image.prefix + " brightfield" + image.suffix, plugin="tifffile")
    first_brightfield = brightfield_im[0,:,:]
    
    fig, ax = plt.subplots()
    ax.imshow(first_brightfield)
    patch = matplotlib.patches.Polygon(xy_coords, closed=True, alpha=0.5, color='red')
    ax.add_patch(patch)
    
    plt.show()
    
def plot_brightfield_with_grid(data_folder, results_folder, image, grid_data):
    
    brightfield_im = skio.imread(data_folder + image.name + "/" + image.prefix + " brightfield" + image.suffix, plugin="tifffile")
    first_brightfield = brightfield_im[0,:,:]
    
    fig, ax = plt.subplots(figsize=(8,8), dpi=256)
    ax.imshow(first_brightfield, cmap='gray', aspect='equal')
    
    line_params = {
        'linewidth': 0.5,
        'color': 'y'
    }
    
    x_max = grid_data["square_x_number"] * grid_data['square_x_size']
    y_max = grid_data["square_y_number"] * grid_data['square_y_size']
    
    ax.set_xlim([0,x_max])
    ax.set_ylim([0,y_max])
    
    ax.set_xticks([])
    ax.set_yticks([])
    
    # vertical lines
    for x_sq_idx in range(int(grid_data["square_x_number"] - 1)):
        x_coord = (x_sq_idx + 1) * grid_data['square_x_size'] - 0.5 # -0.5 ensures line drawn between pixels in adjacent boxes
        ax.plot( [x_coord, x_coord], [0, y_max] , **line_params)
        
    # horizontal lines  
    for y_sq_idx in range(int(grid_data["square_y_number"] - 1)):
        y_coord = (y_sq_idx + 1) * grid_data['square_y_size'] - 0.5
        ax.plot( [0, x_max], [y_coord, y_coord] , **line_params)
    
    fig.tight_layout()
        
    plt.savefig(results_folder + image.prefix + " brightfield_grid.jpg")
    
    