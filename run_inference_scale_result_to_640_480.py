import torch

from imageio import imread, imsave
# from scipy.misc import imresize
import cv2
import numpy as np
from path import Path
import argparse
from tqdm import tqdm

from models import DispResNet
from utils import tensor2array

parser = argparse.ArgumentParser(description='Inference script for DispNet learned with \
                                 Structure from Motion Learner inference on KITTI Dataset',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--output-disp", action='store_true', help="save disparity img")
parser.add_argument("--output-depth", action='store_true', help="save depth img")
parser.add_argument("--pretrained", required=True, type=str, help="pretrained DispResNet path")
parser.add_argument("--img-height", default=256, type=int, help="Image height")
parser.add_argument("--img-width", default=832, type=int, help="Image width")
parser.add_argument("--no-resize", action='store_true', help="no resizing is done")

parser.add_argument("--dataset-list", default=None, type=str, help="Dataset list file")
parser.add_argument("--dataset-dir", default='.', type=str, help="Dataset directory")
parser.add_argument("--output-dir", default='output', type=str, help="Output directory")
parser.add_argument("--img-exts", default=['png', 'jpg', 'bmp'], nargs='*', type=str, help="images extensions to glob")
parser.add_argument('--resnet-layers', required=True, type=int, default=18, choices=[18, 50],
                    help='depth network architecture.')

device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

@torch.no_grad()
def main():
    args = parser.parse_args()
    if not(args.output_disp or args.output_depth):
        print('You must at least output one value !')
        return

    disp_net = DispResNet(args.resnet_layers, False).to(device)
    weights = torch.load(args.pretrained)
    disp_net.load_state_dict(weights['state_dict'])
    disp_net.eval()
    print('running run_inference_scale_result_to_640_480')
    dataset_dir = Path(args.dataset_dir)
    output_dir = Path(args.output_dir)
    output_dir.makedirs_p()

    if args.dataset_list is not None:
        with open(args.dataset_list, 'r') as f:
            test_files = [dataset_dir/file for file in f.read().splitlines()]
    else:
        test_files = sum([dataset_dir.files('*.{}'.format(ext)) for ext in args.img_exts], [])

    print('{} files to test'.format(len(test_files)))

    for file in tqdm(test_files):

        img = imread(file).astype(np.float32)

        h, w, _ = img.shape
        # print('\n height is', h)
        # print('\n width is', w)
        if (not args.no_resize) and (h != args.img_height or w != args.img_width):

            # imresize was deprecated in scipy.misc so i cold either downgrade scipy or
            # replace line below with cv2.resize, which was easier
            img2 = cv2.resize(img, (args.img_width, args.img_height)).astype(np.float32)
            # print('\n np img size is ',img.shape)
        #############################################################################################
        img_transpose = np.transpose(img2, (2, 0, 1))
        print('\n np img_transpose size is ',img_transpose.shape)
        tensor_img = torch.from_numpy(img_transpose).unsqueeze(0)

        # print('\n tensor_img size is ',tensor_img.shape)
        tensor_img = ((tensor_img/255 - 0.45)/0.225).to(device)
        #############################################################################################
        output = disp_net(tensor_img)[0]
        # print('dispnet output size is ',output.shape)
        # print max output value
        # print('max output disparity value is: {}'.format(output.max().item()))

        file_path, file_ext = file.relpath(args.dataset_dir).splitext()
        # file_name = '-'.join(file_path.splitall())
        file_name = ''.join(file_path.splitall())

        if args.output_disp:
            # disp = (255*tensor2array(output, max_value=None, colormap='bone')).astype(np.uint8)
            disp = (255*tensor2array(output, max_value=None, colormap='rainbow')).astype(np.uint8)
            disp_transpose = np.transpose(disp, (1,2,0))

            # imsave(output_dir/'{}_disp{}'.format(file_name, file_ext), disp_transpose)
            # imsave(output_dir/'{}_disp_640_480{}'.format(file_name, file_ext), cv2.resize(disp_transpose,(640,480)))
            # imsave(output_dir/'{}_disp{}'.format(file_name, file_ext), cv2.resize(disp_transpose,(args.img_height,args.img_width)))


        if args.output_depth:

            depth = 1/output
            # depth_array1 = (255*tensor2array(depth, max_value=10, colormap='rainbow')).astype(np.uint8)
            # imsave(output_dir/'{}_depth_max_10{}'.format(file_name, file_ext), np.transpose(depth_array1 , (1, 2, 0)))

            depth_array2 = (255*tensor2array(depth, colormap='bone')).astype(np.uint8)
            dept_transpose = np.transpose(depth_array2, (1, 2, 0))
            # print('max depth after t2a is: {}'.format(depth3.max().item()))
            # print('min depth after t2a is: {}'.format(depth3.min().item()))

            # imsave(output_dir/'{}_depth_max_None{}'.format(file_name, file_ext), dept_transpose)
            imsave(output_dir/'{}_depth_max_None_640_480{}'.format(file_name,file_ext),cv2.resize(dept_transpose,(640,480)))
            print(output_dir,file_name,file_ext)

            # depth = (255*tensor2array(output, max_value=None, colormap='rainbow' )).astype(np.uint8)

            # imsave(output_dir/'{}_depth2{}'.format(file_name, file_ext), np.transpose(depth2, (1, 2, 0)))

if __name__ == '__main__':
    main()
