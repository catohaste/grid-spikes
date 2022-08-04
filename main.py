import matplotlib.pyplot as plt
import matplotlib
import os
import pandas as pd
import numpy as np

import skimage.io as skio

from image_data_as_class import images

from plot import *

root_folder = "/Users/clhastings/Documents/Drive/UCL/Stern/calcium/image_analysis/"
data_folder = "/Users/clhastings/Documents/Drive/UCL/Stern/calcium/image_analysis/ImageJ/"
results_folder = "/Users/clhastings/Documents/Drive/UCL/Stern/calcium/image_analysis/grid_spikes_results/"

# testing
comparison_name = 'testing'
comparison_images = [images[0],images[1]]
image_names_for_plot = ['E1 ant', 'E1 pos']

# define grid
grid = {}
grid["square_x_size"] = 16
grid["square_y_size"] = 16

for image in comparison_images:
    
    im_results_folder = results_folder + "image_data/" + image.name + '/'
    try: # does the results folder exist
        os.mkdir(im_folder)
    except: # results folder already exists
        print("Results folder already exists")
    
    try: # load timeline data
        grid_spikes_results = pd.read_csv(im_results_folder + "cell_grid_timeline.csv")
    except: # no timeline data, so create timeline
        print("No timeline data, so create timeline")
        try: # load image
            
            imstack = skio.imread(data_folder + image.name + "/" + image.name + image.suffix, plugin="tifffile")
            # print(type(imstack), imstack.shape)
            
            image_x_size = imstack.shape[1]
            image_y_size = imstack.shape[2]
            
            grid["square_x_number"] = image_x_size / grid['square_x_size']
            grid["square_y_number"] = image_y_size / grid['square_y_size']
            
            # check image dimensions are divisible by grid size
            if image_x_size % grid["square_x_size"] != 0 or image_y_size % grid["square_y_size"] != 0:
                print("Image size not divisible by grid size", image.prefix)
                
            slice_number = imstack.shape[0]
            
            imageJ_df = pd.read_csv(root_folder + "results/" + image.name + "/cell_grid_timeline.csv")
            compare_dataframe_against_imageJ(imstack, grid, imageJ_df)

        except Exception as e:
            print("Couldn't read image data.")
            print(e)
            
    # plot_brightfield_with_grid(data_folder, im_results_folder, image, grid)

# extract timeline data

# extract peak data