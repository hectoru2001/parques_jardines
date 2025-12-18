from django.urls import path, include
from .views import *

urlpatterns = [
    path('panel/', panel_vista, name="panel_vista"),
    path('gestion-usuarios/', gestion_usuarios, name='gestion_usuarios'),
    path('logs/', ListadoLogs, name="cargarlogs"),
]