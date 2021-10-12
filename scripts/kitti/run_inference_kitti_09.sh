INPUT_DIR=datasets/kitti_odometry/sequences/09/image_2
OUTPUT_DIR=results/kitti_odometry

DISPNET=checkpoints/resnet18_depth_256/dispnet_model_best.pth.tar

python3 run_inference.py \
--pretrained $DISPNET \
--resnet-layers 18 \
--img-height 256 \
--img-width 832 \
--dataset-dir $INPUT_DIR \
--output-dir $OUTPUT_DIR \
--output-disp

# --img-height 370 \
# --img-width 1226 \