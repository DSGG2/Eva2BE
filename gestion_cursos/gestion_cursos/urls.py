from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inscripciones/', include('inscripciones.urls')),
    path('api/',include ('api.urls')),
]
