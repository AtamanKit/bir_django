from rest_framework import routers
from django.urls import path, include
from .views import DeconectViewSet

router = routers.DefaultRouter()
router.register('deconectari', DeconectViewSet)

urlpatterns = [
    path('', include(router.urls))
]