# points to location of RGB images
INPUT_DIR=datasets/tu_delft_husky/report_test_seq

# points to directory to output resulting depth images
OUTPUT_DIR=results/20211116/husky_report_test_seq_r18_husky_320_256_PT_nyu_disp_kitti_pose_9ep/

# points to trained model
DISPNET=checkpoints/r18_husky_320_256_pretrained_kitti_256_disp_and_pose/9ep/dispnet_model_best.pth.tar

# actually run the inference on each image
python3 run_inference_scale_result_to_640_480.py \
--pretrained $DISPNET \
--resnet-layers 18 \
--dataset-dir $INPUT_DIR \
--output-dir $OUTPUT_DIR \
--output-disp \
--output-depth \
--img-width 320 \
--img-height 256



# --dataset-list $LIST_DIR
