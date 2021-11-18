# points to location of RGB images
INPUT_DIR=datasets/tu_delft_husky/report_test_seq

# points to directory to output resulting depth images
OUTPUT_DIR=results/20211116/resnet18_depth_256_1280_960

# points to trained model
DISPNET=checkpoints/resnet18_depth_256/dispnet_model_best.pth.tar

# actually run the inference on each image
python3 run_inference_scale_result_to_640_480.py \
--pretrained $DISPNET \
--resnet-layers 18 \
--dataset-dir $INPUT_DIR \
--output-dir $OUTPUT_DIR \
--output-disp \
--output-depth \
--img-width 1280 \
--img-height 960



# --dataset-list $LIST_DIR
