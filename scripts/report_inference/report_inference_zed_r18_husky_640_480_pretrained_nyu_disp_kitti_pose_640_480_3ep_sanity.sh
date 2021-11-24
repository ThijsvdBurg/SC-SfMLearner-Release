# points to location of RGB images
INPUT_DIR=datasets/tu_delft_husky/report_test_seq

# points to directory to output resulting depth images
OUTPUT_DIR=results/20211119/r18_husky_640_480_pretrained_nyu_disp_kitti_pose_3ep_sanity

# points to trained model
DISPNET=checkpoints/r18_husky_640_480_pretrained_nyu_disp_kitti_pose_sanity/3ep/dispnet_model_best.pth.tar

# actually run the inference on each image
python3 run_inference_scale_result_to_640_480.py \
--pretrained $DISPNET \
--resnet-layers 18 \
--dataset-dir $INPUT_DIR \
--output-dir $OUTPUT_DIR \
--output-disp \
--output-depth \
--img-width 640 \
--img-height 480



# --dataset-list $LIST_DIR
