from django.contrib import admin
from .models import Deranj

@admin.register(Deranj)
class DeranjAdmin(admin.ModelAdmin):
    list_display = ['id', 'transmis', 'sector', 'instalatia', 'pt', 'continutul',
                    'starea']

# admin.site.register(AL)

