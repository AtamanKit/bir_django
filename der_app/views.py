from rest_framework import viewsets
from .serializers import DeranjSerializer
from .models import Deranj

class DeranjViewSet(viewsets.ModelViewSet):
    queryset = Deranj.objects.all()
    serializer_class = DeranjSerializer
