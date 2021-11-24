
# points to location of RGB images
INPUT_DIR=datasets/nyu_test/color

# points to directory to output resulting depth images
OUTPUT_DIR=results/nyu_test/20211124

# LIST_DIR=data/nyu_test_list.txt

# points to trained model
# DISPNET=checkpoints/resnet18_depth_256/dispnet_model_best.pth.tar
DISPNET=checkpoints/rectified_nyu_r18/dispnet_model_best.pth.tar

# actually run the inference on each image
python3 run_inference_scale_result_to_640_480.py \
--pretrained $DISPNET \
--resnet-layers 18 \
--img-height 256 \
--img-width 320 \
--dataset-dir $INPUT_DIR \
--output-dir $OUTPUT_DIR \
--output-depth

# image height and width for NYU data

# 
# --dataset-list $LIST_DIR \
# 