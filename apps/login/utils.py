from apps.administracion.models import LogSistema

def registrar_log(request, accion, usuario=None):
    if usuario is None and request.user.is_authenticated:
        usuario = request.user

    LogSistema.objects.create(
        usuario=usuario,
        accion=accion
    )