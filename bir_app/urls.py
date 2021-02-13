from rest_framework import routers
from django.urls import path, include
from .views import ALViewSet

router = routers.DefaultRouter()
router.register('autorizatii', ALViewSet)

urlpatterns = [
    path('', include(router.urls))
]