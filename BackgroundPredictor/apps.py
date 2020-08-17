import os
import torch
from django.apps import AppConfig
from BackgroundPredictor.DeepImageMatting.loadModel import loadModel

class BackgroundPredictorConfig(AppConfig):
    name = 'BackgroundPredictor'
    
    predictor, device = loadModel()
    # print(predictor)
