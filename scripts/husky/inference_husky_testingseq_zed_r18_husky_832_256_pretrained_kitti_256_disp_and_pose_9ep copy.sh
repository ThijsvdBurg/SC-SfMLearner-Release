
# points to location of RGB images
INPUT_DIR=datasets/tu_delft_husky/zed/testingseq

# points to directory to output resulting depth images
OUTPUT_DIR=results/r18_husky_832_256_pretrained_kitti_256_disp_and_pose/9ep

# points to trained model
DISPNET=checkpoints/r18_husky_832_256_pretrained_kitti_256_disp_and_pose/9ep/dispnet_model_best.pth.tar

# actually run the inference on each image
python3 run_inference.py \
--pretrained $DISPNET \
--resnet-layers 18 \
--dataset-dir $INPUT_DIR \
--output-dir $OUTPUT_DIR \
--output-disp \
--output-depth \
--img-height 832 \
--img-width 256



# --dataset-list $LIST_DIR
