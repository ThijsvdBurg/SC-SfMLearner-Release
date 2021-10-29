TRAIN_SET=datasets/tu_delft_husky/zed/

python train.py $TRAIN_SET \
--folder-type sequence \
--resnet-layers 18 \
--num-scales 1 \
-b1 -s0.1 -c0.5 --epochs 1 \
--with-ssim 1 \
--with-mask 1 \
--with-auto-mask 1 \
--with-pretrain 1 \
--log-output \
--dataset nyu \
--name r18_husky

# -b16 -s0.1 -c0.5 --epoch-size 0 --epochs 50 \