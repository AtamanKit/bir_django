from rest_framework import serializers
from .models import Deranj

class DeranjSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deranj
        fields = ['id',
                  'oficiul',
                  'nr_ordine',
                  'transmis',
                  'sector',
                  'instalatia',
                  'pt',
                  'continutul',
                  'starea',
                 ]