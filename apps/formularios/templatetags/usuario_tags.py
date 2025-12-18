from django import template

register = template.Library()

# Mapeo de grupos a reportes
GRUPO_REPORTES = {
    "riego_chamizal": ["riego_chamizal"],
    "chamizal": ["chamizal"],
    "cuadrilla": ["cuadrilla"],
    "pintura": ["pintura"],
    "fugas": ["fugas"],
    "pipas": ["pipas"],
    "soldadura": ["soldadura"],
    "cultura": ["cultura"],
    "fuentes": ["fuentes"],
}

TODO = ["Supervisor", "Administrador"]

@register.filter(name='tiene_acceso_reporte')
def tiene_acceso_reporte(user, report_slug):
    if user.groups.filter(name__in=TODO).exists():
        return True

    user_groups = [g.name for g in user.groups.all()]
    allowed_groups = GRUPO_REPORTES.get(report_slug, [])

    return any(group in allowed_groups for group in user_groups)

@register.filter
def es_supervisor(user):
    return user.groups.filter(name="Supervisor").exists()

@register.filter
def pertenece(user, grupo_nombre):
    if user.is_authenticated:
        return user.groups.filter(name=grupo_nombre).exists()
    return False

@register.filter
def puede_listar(user):
    return user.groups.filter(name__in=TODO).exists()
