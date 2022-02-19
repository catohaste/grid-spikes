import matplotlib.pyplot as plt
import os
import pandas as pd

from image_data_as_class import images

data_folder = "/Users/clhastings/Documents/Drive/UCL/Stern/calcium/image_analysis/ImageJ/"
results_folder = "/Users/clhastings/Documents/Drive/UCL/Stern/calcium/image_analysis/grid_spikes_results/"

# testing
comparison_name = 'testing'
comparison_images = [images[0],images[1]]
image_names_for_plot = ['E1 ant', 'E1 pos']

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
            I = plt.imread(data_folder + image.name + "/" + image.name + image.suffix)
            
        except Exception as e:
            print("Couldn't read image data.")
            print(e)
    


# define grid

# extract timeline data

# extract peak datao