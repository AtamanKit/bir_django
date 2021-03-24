from rest_framework import viewsets
from .serializers import DeconectSerializer
from .models import Deconect

class DeconectViewSet(viewsets.ModelViewSet):
    queryset = Deconect.objects.all()
    serializer_class = DeconectSerializer
