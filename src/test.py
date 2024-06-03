import numpy as np
import scipy as sp
import torch
import torch.nn as nn
import subprocess

#訓練データ、検証データ、テストデータの読み込み
#(質量数, 陽子数, 中性子数, 陽子ボソン数, 中性子ボソン数, E(0_2^+), E(2_1^+), E(4_1^+), E(6_1^+))
train_data = torch.tensor(np.loadtxt("/home/yutaka/research/data/train_data.csv",delimiter=','),dtype=torch.float32,requires_grad=True)
val_data = torch.tensor(np.loadtxt("/home/yutaka/research/data/val_data.csv",delimiter=','),dtype=torch.float32,requires_grad=True)
test_data = torch.tensor(np.loadtxt("/home/yutaka/research/data/test_data.csv",delimiter=','),dtype=torch.float32,requires_grad=True)




res = subprocess.run("sh /home/yutaka/research/src/test.sh", shell=True)

#乱数seedの設定
seed = 0
torch.manual_seed(seed)


layer1 = nn.Linear(5,16)