from django.db import models

# Create your models here.
class LogSistema(models.Model):
    usuario = models.ForeignKey('auth.User', null=True, blank=True, on_delete=models.SET_NULL)
    accion = models.CharField(max_length=255)
    fecha = models.DateTimeField(auto_now_add=True)