from django.urls import path
from core.views import *

urlpatterns = [
    path('', login),
    path('index/', index),
]
