import numpy as np

def xy_coords_from_raw_coords_for_polygon(raw_coords):

    x_coords = np.array(raw_coords[::2])
    y_coords = np.array(raw_coords[1::2])
    xy_coords = np.column_stack((x_coords, y_coords))
    
    return xy_coords
    
def compare_dataframe_against_imageJ(imstack, grid, imageJ_df):
    
    # create dataframe
    cell_grid_timeline_df = pd.DataFrame(columns=["Mean", "StdDev", "Min", "Max", "BX", "BY", "Median", "Slice", "ROI"])
    
    cell_grid_timeline_test_df = pd.DataFrame(columns=["Mean", "StdDev", "Min", "Max", "BX", "BY", "Width", "Height", "Median", "Slice", "ROI"])
    
    for grid_y_idx in range(2):
    # for grid_y_idx in range(grid.square_y_number):
        BY = grid_y_idx * grid_square_y_size
        for grid_x_idx in range(2):
        # for grid_x_idx in range(grid.square_x_number):
        
            BX = grid_x_idx * grid.square_x_size
            ROI = int(grid_y_idx * grid.square_y_number + grid_x_idx)
            
            # print('BY', BY)
            # print('BX', BX)
            # print('ROI', ROI)
            
            # for t_idx in range(slice_number):
            for t_idx in range(2):
            
                ROI_pixels = imstack[t_idx, BX:BX+grid.square_x_size, BY:BY+grid.square_y_size]
                
                # plt.imshow(ROI_pixels)
                # plt.show()
    
    return