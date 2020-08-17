import os
import cv2
import torch

from BackgroundPredictor.DeepImageMatting.api import pred_pre_trimap, extract_foreground
from BackgroundPredictor.DeepImageMatting.models_v16_4 import DIMModel

checkpoint_name = 'checkpoint.pt'

devices = ['cpu', 'cuda']
device = devices[0]

# Checkpoint folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHECKPOINT_FOLDER = os.path.join(BASE_DIR, 'DeepImageMatting', 'checkpoint')
CHECKPOINT_FILE = os.path.join(CHECKPOINT_FOLDER, checkpoint_name)

def loadModel():
    checkpoint = CHECKPOINT_FILE
    checkpoint = torch.load(checkpoint)
    model = DIMModel()
    model.load_state_dict(checkpoint)
    model = model.to(device)
    model.eval()

    return model, device