
# points to location of RGB images
INPUT_DIR=datasets/tu_delft_husky/testingseq001

# points to directory to output resulting depth images
OUTPUT_DIR=results/r18_husky_640_480_pretrained_nyu_disp_kitti_pose/6ep/testingseq001

# points to trained model
DISPNET=checkpoints/r18_husky_640_480_pretrained_nyu_disp_kitti_pose/6ep/dispnet_model_best.pth.tar

# actually run the inference on each image
python3 run_inference.py \
--pretrained $DISPNET \
--resnet-layers 18 \
--dataset-dir $INPUT_DIR \
--output-dir $OUTPUT_DIR \
--output-disp \
--output-depth \
--img-width 640 \
--img-height 480




# --dataset-list $LIST_DIR
