from django.urls import path

from . import views

urlpatterns = [
    path('prediction', views.list),
    path('prediction/<int:pk>', views.detail),
]