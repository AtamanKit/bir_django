from rest_framework import serializers
from .models import Deconect

class DeconectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deconect
        fields = ['id',
                  'oficiul',
                  'nr_ordine',
                  'pt',
                  'fid_04kv',
                  'data_dec',
                  'data_conect',
                  'durata',
                  'cons_cas',
                  'cons_ec',
                  'total',
                  'cauza',
                  'termen',
                 ]