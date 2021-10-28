
# points to location of RGB images
INPUT_DIR=datasets/tu_delft_husky/zed/seq007
# INPUT_DIR=datasets/nyu_test/color

# points to directory to output resulting depth images
OUTPUT_DIR=results/husky_test_orig_size

# points to trained model
DISPNET=checkpoints/rectified_nyu_r18/dispnet_model_best.pth.tar

# actually run the inference on each image
python3 run_inference.py \
--pretrained $DISPNET \
--resnet-layers 18 \
--dataset-dir $INPUT_DIR \
--output-dir $OUTPUT_DIR \
--output-disp \
--img-height 853 \
--img-width 480


# --output-depth \

# --dataset-list $LIST_DIR
