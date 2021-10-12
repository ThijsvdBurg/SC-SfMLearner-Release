INPUT_DIR=datasets/kitti_depth_test/color
OUTPUT_DIR=results/kitti_depth_test

DISPNET=checkpoints/resnet18_depth_256/dispnet_model_best.pth.tar

python3 run_inference.py \
--pretrained $DISPNET \
--resnet-layers 18 \
--dataset-dir $INPUT_DIR \
--output-dir $OUTPUT_DIR \
--output-disp \
#--no-resize
# --output-depth

# --img-height 370 \
# --img-width 1226 \