TRAIN_SET=datasets/tu_delft_husky/zed/
POSE_NET=checkpoints/r18_husky_832_256_pretrained_nyu_disp_kitti_pose_3ep/exp_pose_model_best.pth.tar
DISP_NET=checkpoints/r18_husky_832_256_pretrained_nyu_disp_kitti_pose_3ep/dispnet_model_best.pth.tar

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
--name r18_husky_640_480_pretrained_nyu_disp_kitti_pose_4-6ep \
--img-width 640 \
--img-height 480 \
--pretrained-pose $POSE_NET \
--pretrained-disp $DISP_NET

# -b16 -s0.1 -c0.5 --epoch-size 0 --epochs 50 \