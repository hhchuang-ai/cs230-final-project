# cs230-final-project
Our poject is built on top of the [Github](https://github.com/taki0112/UGATIT) with some minor tuning/changes. If you want to take the code as reference, please cite the [Paper](https://openreview.net/forum?id=BJlZ5ySKPH) and the [Github](https://github.com/taki0112/UGATIT).

We added some noise in d_loss in UGATIT.py. Every 100 iteration, we will introduce noise into discriminator because the discriminator loss far better than generator noise for our own dataset.

## Tools
resize.py: resize the image to be 256 with jpeg format.

resizePng.py: resize the image to be 256 with png format.

getLoss.py: sieze the statistic data of loss from output log.



Most of the instructions below this line come from the [Github](https://github.com/taki0112/UGATIT).
___
## Requirements
* python == 3.6
* tensorflow == 1.14


## Usage
The structure is as following:
```
├── dataset
   └── YOUR_DATASET_NAME
       ├── trainA
           ├── xxx.jpg (name, format doesn't matter)
           ├── yyy.png
           └── ...
       ├── trainB
           ├── zzz.jpg
           ├── www.png
           └── ...
       ├── testA
           ├── aaa.jpg 
           ├── bbb.png
           └── ...
       └── testB
           ├── ccc.jpg 
           ├── ddd.png
           └── ...
```
PS:
There is a dataset called "sample" for your reference.

### Train
```
> python main.py --dataset selfie2anime --light True
```
* If the memory of gpu is **not sufficient**, set `--light` to **True**
  * But it may **not** perform well
  * paper version is `--light` to **False**

### Test
```
> python main.py --dataset selfie2anime --phase test --light True
```
* If we set `--light` to **True** in training phase, we also need to set up  `--light` to **True** in test phase.

## Tools
resize.py: resize the image to be 256 with jpeg format.

resizePng.py: resize the image to be 256 with png format.

getLoss.py: sieze the statistic data of loss from output log.


## Citation
If you find this code useful for your research, please cite Junho Kim's paper and their Github[link](https://github.com/taki0112/UGATIT):

```
@inproceedings{
Kim2020U-GAT-IT:,
title={U-GAT-IT: Unsupervised Generative Attentional Networks with Adaptive Layer-Instance Normalization for Image-to-Image Translation},
author={Junho Kim and Minjae Kim and Hyeonwoo Kang and Kwang Hee Lee},
booktitle={International Conference on Learning Representations},
year={2020},
url={https://openreview.net/forum?id=BJlZ5ySKPH}
}
```

## Authors of the original paper
[Junho Kim](http://bit.ly/jhkim_ai), Minjae Kim, Hyeonwoo Kang, Kwanghee Lee

