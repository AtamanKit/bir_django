from django.contrib import admin
from .models import AL

@admin.register(AL)
class ALAdmin(admin.ModelAdmin):
    list_display = ['instalatia', 'pt', 'nr_ds', 'nr_al', 'lucrarile',
                    'sef', 'emitent']

# admin.site.register(AL)

