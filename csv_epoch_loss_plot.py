import matplotlib.pyplot as plt
# from mpl_toolkits.axes_grid1 import ImageGrid
import numpy as np
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
parser.add_argument("--input_file", required=True, help="Input csv.")
args = parser.parse_args()
file=args.input_dir

# chdir('/Volumes/macOS Big Sur/Users/pmvanderburg/matplotlib_test/')
# chdir(args.input_dir)
files = listdir(indir)
files.sort()

folders=listdir(indir)

for i, f in enumerate(folders):
    if f=='.DS_Store' or f=='plots':
        del folders[i]
folders.sort()

for fol in folders:
    chdir(path.join(indir,fol))
    files = listdir(path.join(indir,fol))
    for i, fil in enumerate(files):
        if fil=='.DS_Store':
            del files[i]
    files.sort()

    for i, f in enumerate(files):
        if f=='.DS_Store':
            del files[i]

    images = [Image.open(f) for f in files]
    # print(len(images))
    max_rows = 7
    max_cols = 3
    # max_rows = 3
    # max_cols = 2

    methods=['Input image',
             '640x480 N+FT',
             '832x256 K+FT',
             '640x480 N',
             '832x256 N',
             '640x480 K',
             '832x256 K']

    fig, axes = plt.subplots(nrows=4, ncols=1, figsize=(12,10),sharex=True, sharey=True)
    for idx, image in enumerate(images):
        # print(files[idx])
        # print(idx)
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

        axes[row, 0].set_ylabel(methods[row])

    plt.subplots_adjust(wspace=.05, hspace=.05)
    plt.xticks([])
    plt.yticks([])
    filename="three_column_plot_{}.png".format(fol)
    plotpath=path.join(indir,'plots')
    if access(plotpath, W_OK)!=True:
        mkdir(plotpath)

    savepath=path.join(plotpath,filename)
    print('saving in', savepath)
    fig.savefig(savepath)
    # plt.show()
