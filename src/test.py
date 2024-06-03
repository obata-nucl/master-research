import numpy as np
import scipy as sp
import torch
import torch.nn as nn
import subprocess

#訓練データ、検証データ、テストデータの読み込み
train_data = torch.tensor(np.loadtxt("/home/yutaka/research/data/train_data.csv",delimiter=','),dtype=torch.float32,requires_grad=True)
val_data = torch.tensor(np.loadtxt("/home/yutaka/research/data/val_data.csv",delimiter=','),dtype=torch.float32,requires_grad=True)
test_data = torch.tensor(np.loadtxt("/home/yutaka/research/data/test_data.csv",delimiter=','),dtype=torch.float32,requires_grad=True)




res = subprocess.run("sh /home/yutaka/research/src/test.sh", shell=True)