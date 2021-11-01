TRAIN_SET=datasets/tu_delft_husky/zed/
POSE_NET=checkpoints/resnet18_depth_256/exp_pose_model_best.pth.tar
DISP_NET=checkpoints/rectified_nyu_r18/dispnet_model_best.pth.tar

python train.py $TRAIN_SET \
--folder-type sequence \
--resnet-layers 18 \
--num-scales 1 \
-s0.1 -c0.5 --epochs 50 \
--with-ssim 1 \
--with-mask 1 \
--with-auto-mask 1 \
--with-pretrain 1 \
--log-output \
--dataset nyu \
--name r18_husky \
--img-width 480 \
--img-height 640 \
--pretrained-pose $POSE_NET \
--pretrained-disp $DISP_NET

# -b16 -s0.1 -c0.5 --epoch-size 0 --epochs 50 \