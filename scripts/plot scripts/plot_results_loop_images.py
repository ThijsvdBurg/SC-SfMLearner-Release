import matplotlib.pyplot as plt
# from mpl_toolkits.axes_grid1 import ImageGrid
# import numpy as np
from os import listdir
from os import chdir
from os import path
from PIL import Image
from os import access
from os import mkdir
from os import W_OK
# import matplotlib.gridspec as gridspec
import argparse

parser = argparse.ArgumentParser(description="generate plot for report")
parser.add_argument("--input_dir", required=True, help="Input ROS bag.")
parser.add_argument("--figwidth", default=18, type=int)
parser.add_argument("--figheight", default=10, type=int)
parser.add_argument("--rows", required=True, type=int)
parser.add_argument("--cols", required=True, type=int)

args = parser.parse_args()

indir=args.input_dir
# chdir('/Volumes/macOS Big Sur/Users/pmvanderburg/matplotlib_test/')
# chdir(args.input_dir)
files = listdir(indir)
files.sort()

folders=listdir(indir)


for i, f in enumerate(folders):
    if f=='.DS_Store' or f=='plots':
        del folders[i]
folders.sort()
print(folders)
for fol in folders:
    chdir(path.join(indir,fol))
    files = listdir(path.join(indir,fol))
    for i, fil in enumerate(files):
        if fil=='.DS_Store':
            del files[i]
    files.sort()

    delstr = 'husky'
    delstr2 = '640_480_resnet18_depth_256_1280_960'

    for i, f in enumerate(files):
        # print(files[i])
        if f=='.DS_Store':
            del files[i]
        if f.find(delstr)!=-1:
            print(files[i],'will be deleted')
            del files[i]
        if f.find(delstr2)!=-1:
            print(files[i],'will be deleted')
            del files[i]
    files.sort()
    print(len(files),'files left in the list')
    for f in files:
        print(f)

    images = [Image.open(f) for f in files]

    # print(len(images))
    # max_rows = 2
    # max_cols = 3
    figw = args.figwidth
    figh = args.figheight
    max_rows = args.rows
    max_cols = args.cols
    max_im = max_rows * max_cols
    methods=['',
             # 'r18_NYU 320x256',
             # 'r18_NYU 640x480',
             # 'r18_NYU 832x256',
             # 'r18_KITTI 640x480',
             # 'r18_KITTI 832x256',
             '',
             '',
             '',
             '',
             '',
             '',
             '',
             '',
             '']
    print('figw=',figw)
    print('figh=',figh)

    fig, axes = plt.subplots(nrows=max_rows, ncols=max_cols, figsize=(figw,figh),sharex=True, sharey=True)

    for idx, image in enumerate(images):
        print(files[idx])
        if idx==max_im:
            break
        # print('file',idx+1)
        row = idx % max_rows
        col = idx // max_rows
        # print(row,' row')
        # print(col,' col')
        # if col>0:
        # axes[row, col].axis("off")
        axes[row,col].spines['bottom'].set_color('#ffffff')
        axes[row,col].spines['top'].set_color('#ffffff')
        axes[row,col].spines['right'].set_color('#ffffff')
        axes[row,col].spines['left'].set_color('#ffffff')

        if image.size==(1280, 720):
            image = image.resize((640,480))

        axes[row, col].imshow(image, cmap="gray", aspect="auto")

        axes[row, col].set_xlabel(methods[idx],fontsize = 14)
        axes[row, col].xaxis.set_label_position('top')

    plt.subplots_adjust(wspace=.05, hspace=.05)
    plt.xticks([])
    plt.yticks([])
    filename="single_input_PT_output_plot_{}_{}_{}.png".format(figw,figh,fol)
    plotpath=path.join(indir,'plots')
    if access(plotpath, W_OK)!=True:
        mkdir(plotpath)

    savepath=path.join(plotpath,filename)
    print(savepath)
    fig.savefig(savepath,bbox_inches='tight')
    # plt.show()
