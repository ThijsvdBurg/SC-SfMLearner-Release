
import os
import argparse


def main():
    """Extract an image sequence from a rosbag to be used in SC-SfM-learner.
    """
    parser = argparse.ArgumentParser(description="append folder name to image file name.")

    parser.add_argument("--input_dir", required=True, help="Input image directory.")

    example_dir='/Users/pmvanderburg/20211109_copy'

    args = parser.parse_args()

    # print(args.input_dir)
    # print(example_dir, ' is the input directory')
    folders = os.listdir(args.input_dir)
    # folders = os.listdir(example_dir)

    # for f in folders:
        # print(f)


    # self.root = Path(root)
    # scene_list_path = self.root/'train.txt' if train else self.root/'val.txt'
    # self.scenes = [self.root/folder[:-1] for folder in open(scene_list_path)]

    for f in enumerate(folders):

        if f[1] != '.DS_Store':
            # print(f[0])
            # print(f[1])
            path_to_imgs=os.path.join(args.input_dir,f[1])
            imgs = os.listdir(path_to_imgs)
            for i in range(len(imgs)):
                if imgs[i] != '.DS_Store':
                    # print(i)
                    # print(f[1],imgs[i])
                    path_to_img=os.path.join(path_to_imgs,imgs[i])
                    # print(path_to_img)
                    img_no_ext = os.path.splitext(imgs[i])[0]
                    new_name=f"{img_no_ext}_{f[1]}.png"
                    # print('new path is', f"{path_to_imgs}/{img_no_ext}.png")
                    new_path=os.path.join(path_to_imgs,new_name)
                    # print('new path is ',new_path)
                    os.rename(path_to_img, new_path)

            # output_dir/'{}_depth_max_10{}'.format(file_name, file_ext)
            # new_name = os.path.join()
            # print(imgs)
            # rm_path=os.path.join(args.input_dir,filename)
            # imgs = sorted(scene.files('*.png'))
            # os.rename('geeks.txt', 'PythonGeeks.txt')
            # folders = os.listdir(example_dir,'/'.)




    # for idx, image in enumerate(folderlist):
    #     print(idx)

    # for idx, filename in os.listdir(args.input_dir):
    #     print(filename)



if __name__ == '__main__':
    main()
