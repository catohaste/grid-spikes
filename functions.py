import numpy as np

def xy_coords_from_raw_coords_for_polygon(raw_coords):

    x_coords = np.array(raw_coords[::2])
    y_coords = np.array(raw_coords[1::2])
    xy_coords = np.column_stack((x_coords, y_coords))
    
    return xy_coords