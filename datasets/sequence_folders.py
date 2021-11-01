import torch.utils.data as data
import numpy as np
from imageio import imread
from path import Path
import random
import torchvision
import os

def load_as_float(path):
    return imread(path).astype(np.float32)


class SequenceFolder(data.Dataset):
    """A sequence data loader where the files are arranged in this way:
        root/scene_1/0000000.jpg
        root/scene_1/0000001.jpg
        ..
        root/scene_1/cam.txt
        root/scene_2/0000000.jpg
        .
        transform functions must take in a list a images and a numpy array (usually intrinsics matrix)
    """

    def __init__(self, root, seed=None, train=True, sequence_length=3, transform=None, skip_frames=1, dataset='kitti', imgh=480, imgw=640):
        np.random.seed(seed)
        random.seed(seed)
        self.root = Path(root)
        scene_list_path = self.root/'train.txt' if train else self.root/'val.txt'
        self.scenes = [self.root/folder[:-1] for folder in open(scene_list_path)]
        # for folder in open(scene_list_path):
        # print('\n iterating over folder name and type:',folder,type(folder))
        self.transform = transform
        self.dataset = dataset
        self.k = skip_frames
        self.crawl_folders(sequence_length)
        self.imgh = imgh
        self.imgw = imgw

    def crawl_folders(self, sequence_length):
        # k skip frames
        sequence_set = []
        demi_length = (sequence_length-1)//2
        shifts = list(range(-demi_length * self.k, demi_length * self.k + 1, self.k))
        shifts.pop(demi_length)
        for scene in self.scenes:
            # print('scene name and type',scene, type(scene))
            intrinsics = np.genfromtxt(scene/'cam.txt').astype(np.float32).reshape((3, 3))
            # imgs = sorted(scene.files('*.jpg'))
            imgs = sorted(scene.files('*.png'))

            if len(imgs) < sequence_length:
                continue
            for i in range(demi_length * self.k, len(imgs)-demi_length * self.k):
                sample = {'intrinsics': intrinsics, 'tgt': imgs[i], 'ref_imgs': []}
                for j in shifts:
                    sample['ref_imgs'].append(imgs[i+j])
                sequence_set.append(sample)
        random.shuffle(sequence_set)
        self.samples = sequence_set

    def __getitem__(self, index):
        sample = self.samples[index]
        tgt_img = load_as_float(sample['tgt'])
        ref_imgs = [load_as_float(ref_img) for ref_img in sample['ref_imgs']]
        # print('\n \n \n tgt img and refimgs type is: \n \n',type(tgt_img),type(ref_imgs))
        if self.transform is not None:
            imgs, intrinsics = self.transform([tgt_img] + ref_imgs, np.copy(sample['intrinsics']))
            # print('\n \n \n imgs type is: \n \n',type(imgs))
            # print('\n \n \n imgs[1] is: \n \n',imgs[1])
            tgt_img = imgs[0]
            ref_imgs = imgs[1:]
        else:
            intrinsics = np.copy(sample['intrinsics'])

        # print('\n \n \n tgt img and refimgs type is: \n \n',type(tgt_img),type(ref_imgs))
        ########################################################################################################
        img_reshape = torchvision.transforms.Resize((self.imgh,self.imgw))
        tgt_img = img_reshape(tgt_img)
        # print('\n \n \n tgtimg resized shape: ' , tgt_img.shape)
        # ref_imgs = img_reshape(ref_imgs)
        # print('\n \n \n refimg0 resized shape: ' , ref_imgs[0].shape)
        i=0
        for ref_img in ref_imgs:
            # print('\n \n \n refimg type is: \n \n',type(ref_img))
            # print(tgt_img.shape,ref_img.shape)
            ref_img = img_reshape(ref_img)
            ref_imgs[i] = ref_img
            i=i+1

        # print(ref_imgs)
        ########################################################################################################
        return tgt_img, ref_imgs, intrinsics, np.linalg.inv(intrinsics)

    def __len__(self):
        return len(self.samples)
