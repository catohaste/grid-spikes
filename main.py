import matplotlib.pyplot as plt
import matplotlib
import os
import pandas as pd
import numpy as np

import skimage.io as skio

from image_data_as_class import images

data_folder = "/Users/clhastings/Documents/Drive/UCL/Stern/calcium/image_analysis/ImageJ/"
results_folder = "/Users/clhastings/Documents/Drive/UCL/Stern/calcium/image_analysis/grid_spikes_results/"

# testing
comparison_name = 'testing'
comparison_images = [images[0],images[1]]
image_names_for_plot = ['E1 ant', 'E1 pos']

# define grid
grid_square_width = 16

for image in comparison_images:
    
    im_folder = results_folder + "image_data/" + image.name
    try: # does the results folder exist
        os.mkdir(im_folder)
    except: # results folder already exists
        print("Results folder already exists")
    
    try: # load timeline data
        grid_data = pd.read_csv(im_folder + "cell_grid_timeline.csv")
    except: # no timeline data, so create timeline
        print("No timeline data, so create timeline")
        try: # load image
            
            # imstack = skio.imread(data_folder + image.name + "/" + image.name + image.suffix, plugin="tifffile")
            imstack = skio.imread(data_folder + image.name + "/" + image.prefix + " brightfield" + image.suffix, plugin="tifffile")
            print(type(imstack), imstack.shape)
            
            # check image is square
            if imstack.shape[1] != imstack.shape[2]:
                print("Image not square", image.prefix)
            
            # check image dimensions are divisible by grid square size
            if imstack.shape[1] % grid_square_width != 0:
                print("Image width not divisible by grid width", image.prefix)
            
        except Exception as e:
            print("Couldn't read image data.")
            print(e)

# extract timeline data

# extract peak datao