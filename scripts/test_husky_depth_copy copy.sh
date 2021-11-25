DISP_NET=checkpoints/resnet18_depth_256/dispnet_model_best.pth.tar
# DISP_NET=checkpoints/resnet50_depth_256/dispnet_model_best.pth.tar

DATA_ROOT=datasets/tu_delft_husky/zed/report_test_seq
RESULTS_DIR=results/20211109/husky_depth_test/resnet18_depth_256

# test
# python test_disp_edit_vis.py --resnet-layers 18 \
#--img-height 480 --img-width 640 \
#--pretrained-dispnet $DISP_NET \
#--dataset-dir $DATA_ROOT \
#--output-dir $RESULTS_DIR

# evaluate
python eval_depth.py \
--dataset kitti \
--pred_depth=$RESULTS_DIR/predictions.npy \
--gt_depth=$DATA_ROOT/depth
