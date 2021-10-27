
# points to location of RGB images
INPUT_DIR=datasets/tu_delft_husky

# points to directory to output resulting depth images
OUTPUT_DIR=results/husky_test

# LIST_DIR=data/nyu_test_list.txt

# points to trained model
# DISPNET=checkpoints/resnet18_depth_256/dispnet_model_best.pth.tar
DISPNET=checkpoints/rectified_nyu_r18/dispnet_model_best.pth.tar

# actually run the inference on each image
python3 run_inference.py \
--pretrained $DISPNET \
--resnet-layers 18 \
--img-height 480 \
--img-width 640 \
--dataset-dir $INPUT_DIR \
--output-dir $OUTPUT_DIR \
--output-disp

# --output-depth \

# --dataset-list $LIST_DIR