import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
import numpy as np
from os import listdir
from os import chdir
from PIL import Image
import matplotlib.gridspec as gridspec

chdir('/Volumes/macOS Big Sur/Users/pmvanderburg/matplotlib_test/')
files = listdir('/Volumes/macOS Big Sur/Users/pmvanderburg/matplotlib_test/')

images = [Image.open(f) for f in files]


"""
fig = plt.figure()

grid = ImageGrid(fig, 111, # similar to subplot(111)
                nrows_ncols = (2, 5), # creates 2x2 grid of axes
                axes_pad=0.1, # pad between axes in inch.
                )
"""

max_rows = 2
max_cols = 5

fig, axes = plt.subplots(nrows=max_rows, ncols=max_cols, figsize=(20,20))
for idx, image in enumerate(images):
    row = idx // max_cols
    col = idx % max_cols
    axes[row, col].axis("off")
    axes[row, col].imshow(image, cmap="gray", aspect="auto")
plt.subplots_adjust(wspace=.05, hspace=.05)
plt.show()
