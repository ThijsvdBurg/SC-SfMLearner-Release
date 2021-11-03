TRAIN_SET=datasets/tu_delft_husky/zed/
RESNET_FOLDER=checkpoints/rectified_nyu_r18
POSE_NET=$RESNET_FOLDER/exp_pose_model_best.pth.tar
DISP_NET=$RESNET_FOLDER/dispnet_model_best.pth.tar

python train.py $TRAIN_SET \
--folder-type sequence \
--resnet-layers 18 \
--num-scales 1 \
-b4 -s0.1 -c0.5 --epochs 3 \
--with-ssim 1 \
--with-mask 1 \
--with-auto-mask 1 \
--with-pretrain 1 \
--log-output \
--dataset nyu \
--name r18_husky_640_360_pretrained_nyu_disp_and_kitt256_pose \
--img-width 640 \
--img-height 360 \
--pretrained-pose $POSE_NET \
--pretrained-disp $DISP_NET

# -b16 -s0.1 -c0.5 --epoch-size 0 --epochs 50 \