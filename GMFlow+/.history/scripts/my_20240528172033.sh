CUDA_VISIBLE_DEVICES=0 python main_flow.py \
--eval \
--resume pretrained/gmflow-scale1-things-e9887eda.pth \
--val_dataset tub \
--with_speed_metric