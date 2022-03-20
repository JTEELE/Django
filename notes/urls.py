from nturl2path import url2pathname
from django.urls import path

from . import views

urlpatterns = [
    path('notes', views.list),
    path('notes/<int:pk>', views.detail),
]