import os
os.system("python val.py --data data.yaml --weights runs/train/exps/weights/best.pt --img 640") # s模型测试
# os.system("python val.py --data data.yaml --weights runs/train/expm/weights/best.pt --img 640") # m模型测试
# os.system("python val.py --data data.yaml --weights runs/train/expl/weights/best.pt --img 640") # l模型测试
# os.system("python val.py --data data.yaml --weights runs/train/expn/weights/best.pt --img 640") # n模型测试