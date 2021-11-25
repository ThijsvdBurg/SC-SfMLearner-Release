# DISPNET=checkpoints/rectified_nyu_r18/dispnet_model_best.pth.tar

DISPNET=checkpoints/r18_husky_640_480_pretrained_nyu_disp_kitti_pose/9ep/dispnet_model_best.pth.tar

DATA_ROOT=datasets/nyu_test
RESULTS_DIR=results/nyu_self

#  test 256*320 images
python test_disp.py \
--resnet-layers 18 \
--img-width 640 \
--img-height 480 \
--pretrained-dispnet $DISPNET \
--dataset-dir $DATA_ROOT/color \
--output-dir $RESULTS_DIR

# evaluate
python eval_depth.py \
--dataset nyu \
--pred_depth=$RESULTS_DIR/predictions.npy \
--gt_depth=$DATA_ROOT/depth.npy 