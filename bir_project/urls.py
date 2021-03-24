from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('deconect_app/', include('deconect_app.urls')),
    path('der_app/', include('der_app.urls')),
    path('bir_app/', include('bir_app.urls')),
    path('admin/', admin.site.urls),
]
