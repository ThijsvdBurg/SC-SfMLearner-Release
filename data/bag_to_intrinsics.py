#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2021 Delft University of Technology

"""Extract images from a rosbag.
"""

import os
import argparse
import cv2
import rosbag
# from sensor_msgs.msg import Image
from sensor_msgs.msg import CameraInfo
from cv_bridge import CvBridge

def main():
    """Extract an image sequence from a rosbag to be used in SC-SfM-learner.
    """
    parser = argparse.ArgumentParser(description="Extract images from a ROS bag.")

    parser.add_argument("--bag_file", help="Input ROS bag.")
    parser.add_argument("--output_dir", help="Output directory.")
    parser.add_argument("--info_topic", help="camera info topic.")
    # parser.add_argument("--intrinsics_topic", help="Topic containing CameraInfo.")

    args = parser.parse_args()

    print("Extract images from %s on topic %s into %s" % (args.bag_file,args.image_topic, args.output_dir))

    bag = rosbag.Bag(args.bag_file, "r")
    bridge = CvBridge()
    count = 0

    for topic, msg, t in bag.read_messages(topics=[args.info_topic, ]):
        # cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding="passthrough")
        intrinsics = make_camera_msg(msg)
        print("Wrote info %i" % count)

        count += 1

    bag.close()

    return

if __name__ == '__main__':
    main()



def make_camera_msg(cam):
    camera_info_msg = CameraInfo()
    width, height = cam[0], cam[1]
    fx, fy = cam[2], cam[3]
    cx, cy = cam[4], cam[5]
    camera_info_msg.width = width
    camera_info_msg.height = height
    camera_info_msg.K = [fx, 0, cx,
                         0, fy, cy,
                         0, 0, 1]

    camera_info_msg.D = [0, 0, 0, 0]

    camera_info_msg.P = [fx, 0, cx, 0,
                         0, fy, cy, 0,
                         0, 0, 1, 0]
    return camera_info_msg
