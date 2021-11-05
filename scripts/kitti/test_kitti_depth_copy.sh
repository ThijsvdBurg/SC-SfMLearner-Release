<<<<<<< HEAD
DISP_NET=checkpoints/resnet18_depth_256/dispnet_model_best.pth.tar
# DISP_NET=checkpoints/resnet50_depth_256/dispnet_model_best.pth.tar

DATA_ROOT=datasets/kitti_mod
RESULTS_DIR=results/kitti_mod

# test
python test_disp.py --resnet-layers 18 --img-height 256 --img-width 832 \
=======
DISP_NET=checkpoints/
resnet18_depth_256/dispnet_model_best.pth.tar
# DISP_NET=checkpoints/resnet50_depth_256/dispnet_model_best.pth.tar

DATA_ROOT=datasets/kitti_depth_test
RESULTS_DIR=results/kitti_depth_test

# test
python test_disp.py --resnet-layers 18 \
--img-height 256 --img-width 832 \
>>>>>>> 85e5e294034387393396ee4140d10c09a0e254f5
--pretrained-dispnet $DISP_NET --dataset-dir $DATA_ROOT/color \
--output-dir $RESULTS_DIR

# evaluate
<<<<<<< HEAD
python eval_depth.py \
--dataset kitti \
--pred_depth=$RESULTS_DIR/predictions.npy \
--gt_depth=$DATA_ROOT/depth
=======
# python eval_depth.py \
#--dataset kitti \
#--pred_depth=$RESULTS_DIR/predictions.npy \
#--gt_depth=$DATA_ROOT/depth
>>>>>>> 85e5e294034387393396ee4140d10c09a0e254f5
