class Image:
    def __init__(self, image_prefix, embryo_position, sliceN, sub_video_lengths):
        self.prefix = image_prefix
        self.name = image_prefix +  " calcium"
        self.suffix = ".tif"
        self.dim = 1024
        self.position = embryo_position
        self.sliceN = sliceN
        self.sub_video_lengths = sub_video_lengths

###################################################################
""" IMAGE SPECIFIC DATA """
images = []

images.append(Image('2019_07_18 - E1 ant','anterior', 824, [623,201])) # 0
images.append(Image("2019_07_18 - E1 pos",'posterior', 821, [542,279])) # 1
images.append(Image("2019_07_18 - E2 ant",'anterior', 805, [805])) # 2
images.append(Image("2019_07_18 - E2 pos",'posterior', 802, [802])) # 3
images.append(Image("2019_07_18 - E3 ant",'anterior', 808, [808])) # 4
images.append(Image("2019_07_18 - E3 pos",'posterior', 801, [801])) # 5

images.append(Image("2019_07_17 DM whole E1",'anterior', 569, [82, 198, 289])) # 6
images.append(Image("2019_07_17 DM whole E2",'anterior', 601, [601])) # 7
images.append(Image("2019_07_17 DM whole E3",'anterior', 556, [556])) # 8

images.append(Image("2019_07_17 DM bead both E1",'anterior', 1009, [109, 155, 278, 467])) # 9
images.append(Image("2019_07_17 DM bead both E2",'anterior', 658, [658])) # 10

images.append(Image('2019_07_18 - E1 hh2','posterior', 402, [402])) # 11

images.append(Image('2019_07_17 DM bead sep E1 DM','anterior', 185, [101, 84])) # 12
images.append(Image('2019_07_17 DM bead sep E1 control','anterior', 164, [164])) # 13

images.append(Image('2020_01_14 DM bead sep E1 control','anterior', 400, [400])) # 14
images.append(Image('2020_01_14 DM bead sep E1 DM','anterior', 446, [446])) # 15
images.append(Image('2020_01_14 DM bead sep E3 control','anterior', 400, [400])) # 16
images.append(Image('2020_01_14 DM bead sep E3 DM','anterior', 400, [400])) # 17
images.append(Image('2020_01_14 DM bead sep E5 control','anterior', 415, [214,201])) # 18
images.append(Image('2020_01_14 DM bead sep E5 DM','anterior', 401, [401])) # 19
images.append(Image('2020_01_14 DM bead sep E7 control','anterior', 434, [434])) # 20
images.append(Image('2020_01_14 DM bead sep E7 DM','anterior', 435, [435])) # 21
images.append(Image('2020_01_14 DM bead sep E8 control','anterior', 404, [404])) # 22
images.append(Image('2020_01_14 DM bead sep E8 DM','anterior', 400, [400])) # 23

###################################################################
""" EXPERIMENT COMPARISONS """
# testing
comparison_name = 'testing'
comparison_images = [images[0],images[1]]
image_names_for_plot = ['E1 ant', 'E1 pos']

# anterior versus posterior E1
comparison_name = 'ant_vs_pos_E1'
comparison_images = [images[0],images[1]]
image_names_for_plot = ['E1 ant', 'E1 pos']

# anterior versus posterior E2
comparison_name = 'ant_vs_pos_E2'
comparison_images = [images[2],images[3]]
image_names_for_plot = ['E2 ant', 'E2 pos']

# anterior versus posterior E3
comparison_name = 'ant_vs_pos_E3'
comparison_images = [images[4],images[5]]
image_names_for_plot = ['E3 ant', 'E3 pos']

# anterior versus posterior all
comparison_name = 'ant_vs_pos_all'
comparison_images = images[0:6]
image_names_for_title = ['E1 ant', 'E1 pos', 'E2 ant', 'E2 pos', 'E3 ant', 'E3 pos']
image_names_for_plot = ['E1\nant', 'E1\npos', 'E2\nant', 'E2\npos', 'E3\nant', 'E3\npos']
embryo_IDs = ['E1', 'E1', 'E2', 'E2', 'E3', 'E3']

# DM whole mount versus control
comparison_name = 'DM_whole'
comparison_images = [images[0],images[2],images[4],images[6],images[7],images[8]]
image_names_for_title = ['E1 control', 'E2 control', 'E3 control', 'E4 DM', 'E5 DM', 'E6 DM']
image_names_for_plot = ['E1\nctrl', 'E2\nctrl', 'E3\nctrl', 'E4\nDM', 'E5\nDM', 'E6\nDM']

# DM bead sep versus control E1
comparison_name = 'DM_sep_E1'
comparison_images = images[14:16]
image_names_for_plot = ['E1 control', 'E1 DM']
image_names_for_plot = ['E1\nctrl', 'E1\nDM']

# DM bead sep versus control E3
comparison_name = 'DM_sep_E3'
comparison_images = images[16:18]
image_names_for_plot = ['E3 control', 'E3 DM']
image_names_for_plot = ['E3\nctrl', 'E3\nDM']

# DM bead sep versus control E5
comparison_name = 'DM_sep_E5'
comparison_images = images[18:20]
image_names_for_plot = ['E5 control', 'E5 DM']
image_names_for_plot = ['E5\nctrl', 'E5\nDM']

# DM bead sep versus control E7
comparison_name = 'DM_sep_E7'
comparison_images = images[20:22]
image_names_for_plot = ['E7 control', 'E7 DM']
image_names_for_plot = ['E7\nctrl', 'E7\nDM']

# DM bead sep versus control E8
comparison_name = 'DM_sep_E8'
comparison_images = images[22:24]
image_names_for_plot = ['E8 control', 'E8 DM']
image_names_for_plot = ['E8\nctrl', 'E8\nDM']

# DM bead sep versus control 
comparison_name = 'DM_sep'
comparison_images = images[14:24]
image_names_for_title = ['E1 control', 'E1 DM', 'E3 control', 'E3 DM', 'E5 control', 'E5 DM', 'E7 control', 'E7 DM', 'E8 control', 'E8 DM']
image_names_for_plot = ['E1\nctrl', 'E1\nDM', 'E3\nctrl', 'E3\nDM', 'E5\nctrl', 'E5\nDM', 'E7\nctrl', 'E7\nDM', 'E8\nctrl', 'E8\nDM']
embryo_IDs = ['E1', 'E1', 'E3', 'E3', 'E5', 'E5', 'E7', 'E7', 'E8', 'E8']

###################################################################
""" CONTROL COMPARISONS """
