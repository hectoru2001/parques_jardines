from .templatetags.usuario_tags import GRUPO_REPORTES, TODO
from functools import wraps
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect


def requiere_grupo(report_name=None):
    def decorator(view_func):
        @wraps(view_func)
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            user = request.user

            # Si pertenece a un grupo con acceso total
            if user.groups.filter(name__in=TODO).exists():
                return view_func(request, *args, **kwargs)

            # Si se especificó un reporte, validar permisos
            if report_name:
                for group in user.groups.all():
                    reportes = GRUPO_REPORTES.get(group.name, [])
                    if report_name in reportes:
                        return view_func(request, *args, **kwargs)

            # Si no tiene permiso
            messages.error(request, "No tienes permiso de acceder a esta sección.")
            return redirect("main")

        return _wrapped_view
    return decorator

def es_capturista(view_func):

    @wraps(view_func)
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if request.user.groups.filter(name="Captura").exists():
            messages.error(request, "No tienes permiso para acceder a esta sección.")
            return redirect("main")  # o la URL que quieras
        return view_func(request, *args, **kwargs)

    return _wrapped_view