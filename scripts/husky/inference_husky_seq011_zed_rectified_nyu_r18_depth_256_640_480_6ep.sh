
# points to location of RGB images
INPUT_DIR=datasets/tu_delft_husky/zed/seq011

# points to directory to output resulting depth images
OUTPUT_DIR=results/husky_seq011_zed_rectified_nyu_r18_640_480_ep6

# points to trained model
DISPNET=checkpoints/husky_tu_delft_r18_best_6_epochs/dispnet_model_best.pth.tar

# actually run the inference on each image
python3 run_inference.py \
--pretrained $DISPNET \
--resnet-layers 18 \
--dataset-dir $INPUT_DIR \
--output-dir $OUTPUT_DIR \
--output-disp \
--output-depth \
--img-height 480 \
--img-width 640



# --dataset-list $LIST_DIR
