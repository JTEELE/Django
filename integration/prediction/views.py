from django.shortcuts import render
from .models import Predictions

def list(request):
    all_predictions = Predictions.objects.all()
    return render(request, 'prediction/predict_list.html', {'predictions': all_predictions})

def detail(request, pk):
    predict = Predictions.objects.get(pk=pk)
    return render(request, 'prediction/predict_detail.html', {'prediction': predict})
