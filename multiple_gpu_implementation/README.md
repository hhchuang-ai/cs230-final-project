The original code only works for single GPU, so we want to modify it for multiple GPU. We create 2 instances for trainging the model fater. One is p2.xlarge(1 GPU) and another one is p3.16xlarge(8GPU). Ideally, we can have 8~10x speed in p3.16xlarge(8GPU) since the quantity and quality of GPUs in p3.16xlarge is better.

The original code is built on TF 1.14.0, and TF 1.14.0 doesn't have a good support for multiple GPU. Then, We need to change the code manually. After the change, the code works for single GPU. However, when we run it on p3.16xlarge(8GPU), we face the out of memory(OOM) issue. The code cannot distribute the model to 8 GPU evently. Also, the variable scope cannot pass well into different GPU. The data cannot be preload into each GPU evently.

More works are needed for this version. Due to the timely manner, the code implementation is paused.
