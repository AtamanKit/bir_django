from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('bir_app/', include('bir_app.urls')),
    path('admin/', admin.site.urls),
]
