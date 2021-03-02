from rest_framework import routers
from django.urls import path, include
from .views import DeranjViewSet

router = routers.DefaultRouter()
router.register('deranjamente', DeranjViewSet)

urlpatterns = [
    path('', include(router.urls))
]