from rest_framework import viewsets
from .serializers import ALSerializer
from .models import AL

class ALViewSet(viewsets.ModelViewSet):
    queryset = AL.objects.all()
    serializer_class = ALSerializer


