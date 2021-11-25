# points to location of RGB images
INPUT_DIR=datasets/tu_delft_husky/report_test_seq

# points to directory to output resulting depth images
OUTPUT_DIR=results/report_results/20211125_kitti_832_nyu_320_husky_640_and_320/

DISPNET=checkpoints/r18_husky_640_480_pretrained_nyu_disp_kitti_pose/9ep/dispnet_model_best.pth.tar

OUTPUT_NAME=r18_husky_640_480_pretrained_nyu_disp_kitti_pose_9ep

IMW=640

IMH=480
# actually run the inference on each image
python3 run_inference_scale_result_to_640_480.py \
--pretrained $DISPNET \
--resnet-layers 18 \
--dataset-dir $INPUT_DIR \
--output-dir $OUTPUT_DIR \
--output-name $OUTPUT_NAME \
--output-depth \
--img-width $IMW \
--img-height $IMH