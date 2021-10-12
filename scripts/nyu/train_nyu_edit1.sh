# DATA_ROOT=./

TRAIN_SET=datasets/rectified_nyu
DISPNET=checkpoints/rectified_nyu_r18/dispnet_model_best.pth.tar
POSENET=checkpoints/resnet18_depth_256/exp_pose_model_best.pth.tar

python train.py $TRAIN_SET \
--folder-type pair \
--resnet-layers 18 \
--num-scales 1 \
-b 1 \
-s 0.1 \
-c 0.5 \
--epochs 1 \
--with-ssim 1 \
--with-mask 1 \
--with-auto-mask 1 \
--log-output \
--with-gt \
--dataset nyu \
--name rectified_nyu_r18_tbu \
--pretrained-disp $DISPNET \
--pretrained-pose $POSENET \
--with-pretrain 0
# --epoch-size 0