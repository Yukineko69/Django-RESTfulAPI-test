# from django.shortcuts import renderfrom rest_framework import status
import os
import cv2
import numpy as np

from django.conf import settings

from BackgroundPredictor.apps import BackgroundPredictorConfig
from BackgroundPredictor.serializers import FileSerializer

from BackgroundPredictor.DeepImageMatting.api import pred_pre_trimap, pred_trimap, extract_foreground

from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class PredictBackground(APIView):
    parser_class = (FileUploadParser,)
    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            image_path = os.path.join(settings.BASE_DIR + file_serializer.data['image'])
            trimap_path = os.path.join(settings.BASE_DIR + file_serializer.data['trimap'])
            img = cv2.imread(image_path)
            img = img[...,::-1]
            pre_trimap = cv2.imread(trimap_path)
            model = BackgroundPredictorConfig.predictor
            device = BackgroundPredictorConfig.device

            out, scale = pred_pre_trimap(img, pre_trimap, model, device)

            foreground = extract_foreground(img, scale)

            cv2.imwrite('output.jpg', out)
            cv2.imwrite('foreground.jpg', foreground[...,::-1])

            return Response("OK", status=status.HTTP_200_OK)
        
        return Response("Failed", status=status.HTTP_400_BAD_REQUEST)

        # if file_serializer.is_valid():
        #     file_serializer.save()
        #     print('===========================================')
        #     print(settings.BASE_DIR)
        #     print(file_serializer.data['image'])
        #     print(os.path.join(settings.BASE_DIR + file_serializer.data['image']))
        #     print('===========================================')
        #     return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        return Response('Testing', status=status.HTTP_200_OK)
