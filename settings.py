import torch
device = 'cuda' if torch.cuda.is_available() else 'cpu'

NUM_CLASSES = 10
BATCH_SIZE = 256
BATCH_SIZE_MNIST = 256
BATCH_SIZE_MNIST_TEST = 16 #1024
BATCH_SIZE_CIFAR10 = 128

LOAD_CKPT = True # pre_train
NUM_EPOCHS = 100
LEARNING_RATE = 0.001
SCHEDULER_STEP_SIZE = 200

EPS_MINIST = 0.15
EPS_CIFAR10 = 8/255

NUM_WORKERS = 8

CLASSIFY_CKPT = './checkpoint/resnet-Copy1.pth'

# conv 53
MNIST_CKPT = './checkpoint/conv-Copy1.pth'

MOIVE_CKPT = 'checkpoint/model-Copy1.pth'
MOIVE_CKPT_ADV_TRAINING = 'checkpoint/model_adv.pth'

IMAGENET_CKPT = 'checkpoint/imageNet.pth'



