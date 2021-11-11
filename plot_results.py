import matplotlib.pyplot as plt
# from mpl_toolkits.axes_grid1 import ImageGrid
# import numpy as np
from os import listdir
from os import chdir
from PIL import Image
# import matplotlib.gridspec as gridspec
import argparse

parser = argparse.ArgumentParser(description="generate plot for report")
parser.add_argument("--input_dir", required=True, help="Input ROS bag.")
# parser.add_argument("--rows", required=True, help="numer of rows in figure")
# parser.add_argument("--cols", required=True, help="number of columns in figure")

args = parser.parse_args()

# chdir('/Volumes/macOS Big Sur/Users/pmvanderburg/matplotlib_test/')
chdir(args.input_dir)
files = listdir(args.input_dir)

for i, f in enumerate(files):
    if f!='.DS_Store':
        print(i,f)
    else:
        del files[i]

images = [Image.open(f) for f in files]

# max_rows = args.rows
# max_cols = args.cols
max_rows = 6
max_cols = 1

fig, axes = plt.subplots(nrows=max_rows, ncols=max_cols, figsize=(4,10))#,sharex=True, sharey=True)
for idx, image in enumerate(images):
    # print(files[idx])
    # print(idx)
    row = idx // max_cols
    col = idx % max_cols

    print(row, col, 'row, col')
    if col>0:
        axes[row, col].axis("off")
    # axes[row, col].imshow(image, cmap="gray", aspect="auto")

    axes[0,0].set_ylabel('common Y')
plt.subplots_adjust(wspace=.05, hspace=.05)
plt.xticks([])
plt.yticks([])
# plt.setp(axes[:, 0], ylabel='y axis label')
plt.show()
