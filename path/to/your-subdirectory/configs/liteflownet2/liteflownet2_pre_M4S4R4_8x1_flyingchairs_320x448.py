_base_ = [
    '../_base_/models/liteflownet2/liteflownet2_pre_M4S4R4.py',
    '../_base_/datasets/flyingchairs_320x448.py',
    '../_base_/default_runtime.py'
]

optimizer = dict(type='Adam', lr=1e-4, weight_decay=0.0004, betas=(0.9, 0.999))
optimizer_config = dict(grad_clip=None)
# learning policy
lr_config = dict(
    policy='step', by_epoch=False, gamma=0.5, step=[120000, 160000, 200000])
runner = dict(type='IterBasedRunner', max_iters=240000)
checkpoint_config = dict(by_epoch=False, interval=40000)
evaluation = dict(interval=40000, metric='EPE')

# Weights are initialized from model of previous stage
load_from = 'https://download.openmmlab.com/mmflow/liteflownet2/liteflownet2_pre_M5S5R5_8x1_flyingchairs_320x448.pth'  # noqa
