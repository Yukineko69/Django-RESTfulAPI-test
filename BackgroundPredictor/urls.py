from django.urls import path
import BackgroundPredictor.views as views

urlpatterns = [
    path('predict_bg/', views.PredictBackground.as_view(), name='predict_background'),
]