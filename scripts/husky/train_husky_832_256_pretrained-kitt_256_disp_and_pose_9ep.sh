TRAIN_SET=datasets/tu_delft_husky/zed/
RESNET_FOLDER=checkpoints/r18_husky_832_256_pretrained_kitti_256_disp_and_pose//11-03-10_00_6ep
POSE_NET=$RESNET_FOLDER/exp_pose_model_best.pth.tar
DISP_NET=$RESNET_FOLDER/dispnet_model_best.pth.tar

python train.py $TRAIN_SET \
--folder-type sequence \
--resnet-layers 18 \
--num-scales 1 \
-s0.1 -c0.5 --epochs 3 \
--with-ssim 1 \
--with-mask 1 \
--with-auto-mask 1 \
--with-pretrain 1 \
--log-output \
--dataset nyu \
--name r18_husky_832_256_pretrained_kitti_256_disp_and_pose \
--img-width 832 \
--img-height 256 \
--pretrained-pose $POSE_NET \
--pretrained-disp $DISP_NET

# -b16 -s0.1 -c0.5 --epoch-size 0 --epochs 50 \