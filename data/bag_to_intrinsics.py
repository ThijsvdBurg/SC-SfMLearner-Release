#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2021 Delft University of Technology

"""Extract images from a rosbag.
"""

import os
import argparse
# import cv2
import rosbag
# from sensor_msgs.msg import Image
# from sensor_msgs.msg import CameraInfo
# from cv_bridge import CvBridge

def main():
    """Extract an image sequence from a rosbag to be used in SC-SfM-learner.
    """
    parser = argparse.ArgumentParser(description="Extract images from a ROS bag.")

    parser.add_argument("--bag_file", help="Input ROS bag.")
    parser.add_argument("--output_dir", help="Output directory.")
    parser.add_argument("--info_topic", help="camera info topic.")
    # parser.add_argument("--intrinsics_topic", help="Topic containing CameraInfo.")

    args = parser.parse_args()

    # print("Extract images from %s on topic %s into %s" % (args.bag_file,args.image_topic, args.output_dir))

    bag = rosbag.Bag(args.bag_file, "r")
    # bridge = CvBridge()
    count = 3
    # count = 0

    for topic, msg, t in bag.read_messages(topics=[args.info_topic]):
        # cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding="passthrough")
        camera_info_msg = make_camera_msg(msg)
        K = camera_info_msg.K
        print(type(K))
        print("Wrote info %i" % count)

        # count += 1
        count -= 1

    bag.close()

    return

if __name__ == '__main__':
    main()



