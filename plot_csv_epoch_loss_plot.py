import matplotlib.pyplot as plt
plt.style.use(['science','bright'])
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
parser.add_argument("--output_dir", required=True, help="output dir for plot.")
args = parser.parse_args()

file=args.input_file
outdir=args.output_dir

data= np.genfromtxt(file, delimiter=';',  skip_header=2, names=['x','NK640_train','NK640_val','KK832_train','KK832_val'])

fig=plt.figure()
ax1 = fig.add_subplot(111)

ax1.set_title("Finetuning the two promising configurations")
ax1.set_xlabel('Epochs')
ax1.set_ylabel('Loss')

ax1.plot(data['x'], data['NK640_train'], c='r',                 label='640x480 N training')
ax1.plot(data['x'], data['NK640_val'], c='b',                   label='640x480 N validation')
ax1.plot(data['x'], data['KK832_train'], c='r',linestyle='-.',  label='832x256 K training')
ax1.plot(data['x'], data['KK832_val'], c='b',  linestyle='-.',  label='832x256 K validation')
#
# ax1.plot(data['x'], data['NK640_train'],                 label='640x480 N training')
# ax1.plot(data['x'], data['NK640_val'],                   label='640x480 N validation')
# ax1.plot(data['x'], data['KK832_train'],linestyle='-.',  label='832x256 K training')
# ax1.plot(data['x'], data['KK832_val'],  linestyle='-.',  label='832x256 K validation')

ax1.legend()

# plt.show()

filename="epoch_plot_2.png"
plotpath=path.join(outdir,'plots')
if access(plotpath, W_OK)!=True:
    mkdir(plotpath)

savepath=path.join(plotpath,filename)
print('saving in', savepath)
fig.savefig(savepath)
# plt.show()
