from django import template

register = template.Library()

# Mapeo de grupos a reportes
GRUPO_REPORTES = {
    "1": ["Riego Chamizal"],
    "2": ["Reporte Chamizal"],
    "3": ["Riego Chamizal", "Reporte Chamizal"],
    "4": ["Reporte Cuadrilla"],
    "5": ["Reporte Pintura"],
    "6": ["Reporte Fugas", "Reporte Cuadrilla"],
    "7": ["Soldadura"],
}

TODO = ["Supervisor", "Administrador"]

@register.filter(name='tiene_acceso_reporte')
def tiene_acceso_reporte(user, report_name):
    if user.groups.filter(name__in=TODO).exists():
        return True

    for group in user.groups.all():
        if group.name in GRUPO_REPORTES:
            if report_name in GRUPO_REPORTES[group.name]:
                return True
    return False


@register.filter
def puede_listar(user):
    return user.groups.filter(name__in=TODO).exists()
