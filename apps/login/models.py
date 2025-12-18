from django.db import models

# Create your models here.
class UsuariosInfo(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    tipo_usuario = models.IntegerField(default=2, choices=[
        (0, 'Superadmin'),
        (1, 'Administrador'),
        (2, 'Usuario'),
        (3, 'Invitado'),
    ])
