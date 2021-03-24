from django.contrib import admin
from .models import Deconect

@admin.register(Deconect)
class DeconectAdmin(admin.ModelAdmin):
    list_display = ['id', 'oficiul', 'pt', 'durata', 'cons_cas', 'cons_ec',
                    'cauza']
