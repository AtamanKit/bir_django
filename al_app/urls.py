from django.urls import path
from . import views

urlpatterns = [
    path('', views.al, name='al'),
]