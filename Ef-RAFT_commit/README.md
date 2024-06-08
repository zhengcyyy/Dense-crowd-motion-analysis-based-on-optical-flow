# Ef-RAFT
 	
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/rethinking-raft-for-efficient-optical-flow/optical-flow-estimation-on-sintel-clean)](https://paperswithcode.com/sota/optical-flow-estimation-on-sintel-clean?p=rethinking-raft-for-efficient-optical-flow)


 	
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/rethinking-raft-for-efficient-optical-flow/optical-flow-estimation-on-kitti-2015-train)](https://paperswithcode.com/sota/optical-flow-estimation-on-kitti-2015-train?p=rethinking-raft-for-efficient-optical-flow)

 	
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/rethinking-raft-for-efficient-optical-flow/optical-flow-estimation-on-sintel-final)](https://paperswithcode.com/sota/optical-flow-estimation-on-sintel-final?p=rethinking-raft-for-efficient-optical-flow)

This repository contains the source code for [Ef-RAFT: Rethinking RAFT for Efficient Optical Flow](https://arxiv.org/abs/2401.00833)<br/>

<img src="Diagram.png">

## Requirements
The code has been tested with PyTorch 1.6 and Cuda 10.1.
```Shell
conda create --name efraft
conda activate raft
conda install pytorch=1.6.0 torchvision=0.7.0 cudatoolkit=10.1 matplotlib tensorboard scipy opencv -c pytorch
```


## Required Data
To evaluate/train RAFT, you will need to download the required datasets and put them in ```datasets/``` directory. 
* [FlyingChairs](https://lmb.informatik.uni-freiburg.de/resources/datasets/FlyingChairs.en.html#flyingchairs)
* [FlyingThings3D](https://lmb.informatik.uni-freiburg.de/resources/datasets/SceneFlowDatasets.en.html)
* [Sintel](http://sintel.is.tue.mpg.de/)
* [KITTI](http://www.cvlibs.net/datasets/kitti/eval_scene_flow.php?benchmark=flow)

## How to run?
For training on 2 GPUs, run the following command. Training logs will be written to the `runs` directory, which can be visualized using tensorboard.
```Shell
./train_standard.sh
```

For running on a single RTX GPU, training can be accelerated using mixed precision, and can be done with the following command. You can expect similiar results in this setting (1 GPU).
```Shell
./train_mixed.sh
```

You can evaluate a trained model using `evaluate.py`.
```Shell
python evaluate.py --model=models/raft-things.pth --dataset=sintel --mixed_precision
```

### Quantitative Results
Comparison of the proposed method with existing
techniques on the Sintel and KITTI datasets. Metrics in green, blue, and
red denote the first, second, and third-best results, respectively.
<p align="center">
<img src="Results.png" width="700" height="500">
<p/>


### Qualitative Results
Qualitative comparison between the proposed method and RAFT. Frames with orange and blue labels are from Sintel
and KITTI datasets, respectively.
<img src="Visualization.png">


 ## Citation
If you use this repository for your research or wish to refer to our method, please use the following BibTeX entry:
```bibtex
@article{eslami2024rethinking,
  title={Rethinking RAFT for Efficient Optical Flow},
  author={Eslami, Navid and Arefi, Farnoosh and Mansourian, Amir M and Kasaei, Shohreh},
  journal={arXiv preprint arXiv:2401.00833},
  year={2024}
}
```

### Acknowledgement
This codebase is heavily borrowed from [RAFT: Recurrent All Pairs Field Transforms for Optical Flow](https://github.com/princeton-vl/RAFT). Thanks for their excellent work.

### TUB数据集测试
采用ours-things.pth权重效果最优

使用以下命令进行测试：
```Shell
python evaluate.py --model=models/ours-things.pth --dataset=TUB --mixed_precision
```

对不同光流场测试请修改evaluate.py中validate_TUB中valid_dataset初始化参数*name*

得到结果如下

| Flow name | EPE  | AE   | IE    |
|-----------|------|------|-------|
| IM01      | 0.44 | 1.47 | 44.44 |
| IM01_hDyn | 2.64 | 1.47 | 66.26 |
| IM02      | 0.33 | 1.47 | 42.84 |
| IM02_hDyn | 2.37 | 1.48 | 68.50 |
| IM03      | 0.26 | 1.46 | 42.97 |
| IM03_hDyn | 2.49 | 1.47 | 76.03 |
| IM04      | 0.26 | 1.52 | 38.06 |
| IM04_hDyn | 3.38 | 1.52 | 80.58 |
| IM05      | 1.27 | 1.28 | 67.12 |
| IM05_hDyn | 6.22 | 1.39 | 84.73 |

考虑到迁移到武汉地铁人群数据集，选择摄像头机位不变数据集进行finetune，sequenceloss从0.52下降到0.20，得到结果如下

| Flow name | EPE  | AE   | IE    |
|-----------|------|------|-------|
| IM01      | 0.10 | 1.47 | 19.41 |
| IM01_hDyn | 0.26 | 1.48 | 29.74 |
| IM02      | 0.12 | 1.47 | 15.92 |
| IM02_hDyn | 0.48 | 1.49 | 31.57 |
| IM03      | 0.08 | 1.47 | 19.29 |
| IM03_hDyn | 0.54 | 1.49 | 40.71 |
| IM04      | 0.11 | 1.51 | 13.30 |
| IM04_hDyn | 0.33 | 1.52 | 28.34 |
| IM05      | 0.32 | 1.29 | 34.04 |
| IM05_hDyn | 1.79 | 1.43 | 47.30 |

同时发现在机位可变数据集表现有提升