# Uses DualGAN Architecture
 
# ICCV paper of DualGAN
<a href="https://arxiv.org/abs/1704.02510">DualGAN: unsupervised dual learning for image-to-image translation</a>

please cite the paper, if the codes has been used for your research.

# architecture of DualGAN

![architecture](https://github.com/duxingren14/DualGAN/blob/master/0.png)

# How to setup

## Prerequisites

* Linux / Windows

* Python (2.7 or later)

* numpy: `pip install numpy`

* scipy: 

* NVIDIA GPU + CUDA 8.0 + CuDNN v5.1

* TensorFlow 1.0 or later


# Getting Started
## steps

* Clone this repo:
1. `git clone https://github.com/Python-is-better-than-Java/Stick-Figure-to-Real-Life-Animation.git`
2. `cd Stick-Figure-to-Real-Life-Animation`

* Convert stick figure animation to real-life video:
1. Insert a stick figure animation (video name can be anything as long as it is of MP4 format) into the main folder.
2. In terminal, type the following: 
`python main.py --phase test --dataset_name sketch-photo --image_size 256 --lambda_A 1000.0 --lambda_B 1000.0 --epoch 100`
3. The real-life video will be named "Real_Life_Animation.mp4".

Note: Before starting, ensure that there is no other video except for the stick-figure video you intend to use.

# Acknowledgments

Codes are built on the top of pix2pix-tensorflow and DCGAN-tensorflow. Thanks for their precedent contributions!
