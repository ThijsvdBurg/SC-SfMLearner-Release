#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2021 Delft University of Technology

"""remove 9 out of 10 frames to reduce results size.
"""

import os
import argparse


def main():
    """Extract an image sequence from a rosbag to be used in SC-SfM-learner.
    """
    parser = argparse.ArgumentParser(description="delete every 9 images out of 10.")

    parser.add_argument("--input_dir", help="Input ROS bag.")

    args = parser.parse_args()

    print(args.input_dir)

    dl_number=[]
    for i in range(1,10,1):
        dl_number.append(i)

    print(dl_number)

    for x in dl_number:
            print(x)

    for i in range(0,10,1):
            for x in dl_number:
                    filename="0000{0}{1}.png".format(i,x)
                    rm_path=os.path.join(args.input_dir,filename)
                    print(rm_path)
                    if os.access(rm_path, os.R_OK):
                            os.remove(rm_path)
                            print(rm_path,' deleted successfully')

    return

if __name__ == '__main__':
    main()



