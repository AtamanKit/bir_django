from django.urls import path
from . import views

urlpatterns = [
    path('', views.oficii, name='oficii'),
]