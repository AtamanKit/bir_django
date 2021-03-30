from rest_framework import serializers
from .models import AL

class ALSerializer(serializers.ModelSerializer):
    class Meta:
        model = AL
        fields = ['id',
                  'oficiul',
                  'nr_ds',
                  'nr_al',
                  'instalatia',
                  'pt',
                  'localitatea',
                  'fid_nr',
                  'lucrarile',
                  'sef',
                  'mem_ech',
                  'emitent',
                  'cu_dec',
                  'mas_teh',
                  'semnatura',
                  'starea',
                  'pregatire',
                  'admitere',
                  'terminare',
                  'link',
        ]