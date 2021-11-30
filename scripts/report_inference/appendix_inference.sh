# points to location of RGB images
INPUT_DIR=datasets/tu_delft_husky/f_ed_up

# points to directory to output resulting depth images
OUTPUT_DIR=results/appendix_inference

DISPNET=checkpoints/resnet18_depth_256/dispnet_model_best.pth.tar

IMW=640
IMH=480
# actually run the inference on each image
python3 run_inference_original.py \
--pretrained $DISPNET \
--resnet-layers 18 \
--dataset-dir $INPUT_DIR \
--output-dir $OUTPUT_DIR \
--output-name appendix_inference \
--output-depth \
--img-width $IMW \
--img-height $IMH

IMW=832
IMH=256
# actually run the inference on each image
python3 run_inference_original.py \
--pretrained $DISPNET \
--resnet-layers 18 \
--dataset-dir $INPUT_DIR \
--output-dir $OUTPUT_DIR \
--output-name appendix_inference \
--output-depth \
--img-width $IMW \
--img-height $IMH