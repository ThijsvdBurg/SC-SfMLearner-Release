
# points to location of RGB images
INPUT_DIR=datasets/tu_delft_husky/testingseq

# points to directory to output resulting depth images
OUTPUT_DIR=results/husky_testingseq_zed_rectified_nyu_r18_480_640

# points to trained model
DISPNET=checkpoints/rectified_nyu_r18/dispnet_model_best.pth.tar

# actually run the inference on each image
python3 run_inference.py \
--pretrained $DISPNET \
--resnet-layers 18 \
--dataset-dir $INPUT_DIR \
--output-dir $OUTPUT_DIR \
--output-disp \
--output-depth \
--img-width 480 \
--img-height 640



# --dataset-list $LIST_DIR
