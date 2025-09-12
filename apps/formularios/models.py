from django.db import models

class ReporteCuadrilla(models.Model):
    # Datos generales
    distrito = models.CharField(max_length=100)
    dia = models.CharField(max_length=20, blank=True)
    fecha = models.DateField()
    trabajo_realizado = models.TextField(blank=True, null=True)

    coordinador = models.CharField(max_length=100)
    encargado_cuadrilla = models.CharField(max_length=100)

    # Áreas atendidas
    parques_comunitarios = models.BooleanField(default=0)
    parques_municipales = models.BooleanField(default=0)
    monumentos_atendidos = models.BooleanField(default=0)
    camellones_atendidos = models.BooleanField(default=0)
    apoyo_areas_gob = models.BooleanField(default=0)
    otros = models.CharField(max_length=20, blank=True, null=True)
    otros_cant = models.BooleanField(default=0)



    # Superficies y trabajos
    superficie_atendida_m2 = models.IntegerField(default=0)
    cesped_cortado_m2 = models.IntegerField(default=0)
    deshierbe_m2 = models.IntegerField(default=0)
    arboles_plantados = models.IntegerField(default=0)
    arboles_podados = models.IntegerField(default=0)
    arboles_retirados = models.IntegerField(default=0)
    zacate_basura_kilos = models.IntegerField(default=0)
    escombro_kilos = models.IntegerField(default=0)
    llantas_recolectadas = models.IntegerField(default=0)
    papeleo_m2 = models.IntegerField(default=0)
    personal_trabajo = models.IntegerField(default=0)

    #Recursos
    equipo_utilizado = models.TextField(blank=True, null=True)
    material_utilizado = models.TextField(blank=True, null=True)
    vehiculos_utilizados = models.TextField(blank=True, null=True)

    # Evaluaciones de condición (opciones SI/NO/MALO/REGULAR/BUENO/EXCELENTE)
    OPCIONES_EVALUACION = [
        ("SI", "Sí"),
        ("NO", "No"),
        ("MALO", "Malo"),
        ("REGULAR", "Regular"),
        ("BUENO", "Bueno"),
        ("EXCELENTE", "Excelente"),
    ]

    pintura_juegos = models.CharField(max_length=10, choices=OPCIONES_EVALUACION, blank=True)
    cuenta_alumbrado = models.CharField(max_length=10, choices=OPCIONES_EVALUACION, blank=True)
    cuenta_jueguitos = models.CharField(max_length=10, choices=OPCIONES_EVALUACION, blank=True)
    cuenta_mobiliario = models.CharField(max_length=10, choices=OPCIONES_EVALUACION, blank=True)
    cuenta_sistema_riego = models.CharField(max_length=10, choices=OPCIONES_EVALUACION, blank=True)
    necesita_reforestacion = models.CharField(max_length=10, choices=OPCIONES_EVALUACION, blank=True)

    OPCIONES_FRECUENCIA = [
        ("1", "1 VEZ POR SEMANA"), 
        ("2", "2 VECES POR SEMANA"), 
        ("3", "3 VECES POR SEMANA"), 
        ("0", "NUNCA")
    ]

    frecuncia_recoleccion_basura = models.CharField(max_length=25, choices=OPCIONES_FRECUENCIA, blank=True)

    # Observaciones
    observaciones_parque = models.TextField(blank=True, null=True)
    otras_observaciones = models.TextField(blank=True, null=True)
    pendientes = models.TextField(blank=True, null=True)

    # Ubicación
    ubicacion_area = models.CharField(max_length=200, blank=True, null=True)
    colonia_camellon = models.CharField(max_length=200, blank=True, null=True)
    calle = models.CharField(max_length=200, blank=True, null=True)

    # Tipo de trabajo
    trabajo_diario = models.BooleanField(default=False)
    trabajo_ciudadania = models.BooleanField(default=False)
    operativo_especial = models.BooleanField(default=False)


    def __str__(self):
        return f"Reporte {self.numero_reporte} - {self.dia}"


class ReporteChamizal(models.Model):
    distrito = models.CharField(max_length=100)
    fecha = models.DateField()
    dia = models.CharField(max_length=20, blank=True)

    trabajo_diario = models.BooleanField(default=False)
    trabajo_ciudadania = models.BooleanField(default=False)
    operativo_especial = models.BooleanField(default=False)

    coordinador = models.CharField(max_length=100)
    encargado_cuadrilla = models.CharField(max_length=100)

    parque_chamizal = models.BooleanField(default=False)
    hoyos = models.BooleanField(default=False)
    camellones = models.BooleanField(default=False)
    otros = models.CharField(max_length=20, blank=True, null=True)
    otros_bool = models.BooleanField(default=False)

    superficie_atendida_m2 = models.IntegerField(default=0)
    cesped_cortado_m2 = models.IntegerField(default=0)
    deshierbe_m2 = models.IntegerField(default=0)
    arboles_plantados = models.IntegerField(default=0)
    arboles_podados = models.IntegerField(default=0)
    arboles_retirados = models.IntegerField(default=0)
    zacate_basura_kilos = models.IntegerField(default=0)
    papeleo_m2 = models.IntegerField(default=0)
    personal_trabajo = models.IntegerField(default=0)

    trabajo_realizado = models.TextField(blank=True, null=True)
    pendientes = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    ubicacion_area = models.CharField(max_length=200, blank=True, null=True)

    equipo_utilizado = models.TextField(blank=True, null=True)
    material_utilizado = models.TextField(blank=True, null=True)
    vehiculos_utilizados = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Reporte Chamizal"

class ReporteCultura(models.Model):
    fecha = models.DateField()
    dia = models.CharField(max_length=20, blank=True)
    encargado = models.CharField(max_length=100, blank=True)
    lugar = models.CharField(max_length=100, blank=True)

    personas_beneficiadas = models.IntegerField(default=0)
    escuela_atendida = models.CharField(max_length=100, blank=True)
    maquiladora_atendida = models.CharField(max_length=100, blank=True)
    platica_sustentabilidad = models.CharField(max_length=100, blank=True)
    curso_poda = models.CharField(max_length=100, blank=True)
    comite_parque = models.CharField(max_length=100, blank=True)

    colonia = models.CharField(max_length=100, blank=True)
    calle1 = models.CharField(max_length=100, blank=True)
    calle2 = models.CharField(max_length=100, blank=True)
    calle3 = models.CharField(max_length=100, blank=True)
    calle4 = models.CharField(max_length=100, blank=True)

    observaciones = models.TextField(blank=True, null=True)
    responsable = models.CharField(max_length=100, blank=True)
    nombre_ciudadano = models.CharField(max_length=100, blank=True)

class ReporteFuentes(models.Model):
    fecha = models.DateField()
    dia = models.CharField(max_length=20, blank=True)
    coordinador = models.CharField(max_length=100, blank=True)
    encargado = models.CharField(max_length=100, blank=True)
    superficie_atendida_m2 = models.IntegerField(default=0)
    limpieza_papeleo_m2 = models.IntegerField(default=0)
    reparacion_tuberia = models.IntegerField(default=0)
    basura_kg = models.IntegerField(default=0)

    reparacion_bomba = models.IntegerField(default=0)
    instalacion_bomba = models.IntegerField(default=0)
    personal_trabajo = models.IntegerField(default=0)

    colonia = models.CharField(max_length=100, blank=True)
    calle1 = models.CharField(max_length=100, blank=True)
    calle2 = models.CharField(max_length=100, blank=True)
    observaciones = models.TextField(blank=True, null=True)

class ReporteFugas(models.Model):
    distrito = models.CharField(max_length=100)
    fecha = models.DateField()
    dia = models.CharField(max_length=20, blank=True)

    trabajo_diario = models.BooleanField(default=False)
    trabajo_ciudadania = models.BooleanField(default=False)
    operativo_especial = models.BooleanField(default=False)

    coordinador = models.CharField(max_length=100)
    encargado_cuadrilla = models.CharField(max_length=100)

    parques_comunitarios = models.BooleanField(default=0)
    parques_municipales = models.BooleanField(default=0)
    monumentos_atendidos = models.BooleanField(default=0)
    camellones_atendidos = models.BooleanField(default=0)
    apoyo_areas_gob = models.BooleanField(default=0)
    otros = models.CharField(max_length=20, blank=True, null=True)
    otros_cant = models.BooleanField(default=0)

    superficie_atendida_m2 = models.IntegerField(default=0)
    reparacion_fugas = models.IntegerField(default=0)
    instalacion_agua = models.IntegerField(default=0)
    instalacion_riego = models.IntegerField(default=0)
    revision_riego = models.IntegerField(default=0)
    material_riego = models.IntegerField(default=0)
    personal_trabajo = models.IntegerField(default=0)

    trabajo_realizado = models.TextField(blank=True, null=True)
    pendientes = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    colonia = models.CharField(max_length=100, blank=True)
    calle1 = models.CharField(max_length=100, blank=True)
    calle2 = models.CharField(max_length=100, blank=True)

    equipo_utilizado = models.TextField(blank=True, null=True)
    material_utilizado = models.TextField(blank=True, null=True)
    vehiculos_utilizados = models.TextField(blank=True, null=True)

class ReportePintura(models.Model):
    fecha = models.DateField()
    dia = models.CharField(max_length=20, blank=True)
    distrito = models.CharField(max_length=100)
    encargado = models.CharField(max_length=100, blank=True)
    coordinador = models.CharField(max_length=100, blank=True)
    trabajo_diario = models.BooleanField(default=False)
    trabajo_ciudadania = models.BooleanField(default=False)
    operativo_especial = models.BooleanField(default=False)

    comunitarios_atendidos = models.BooleanField(default=0)
    municipales_atendidos = models.BooleanField(default=0)
    monumentos_atendidos = models.BooleanField(default=0)
    camellones_atendidos = models.BooleanField(default=0)
    apoyo_areas_gob = models.BooleanField(default=0)
    otros = models.CharField(max_length=20, blank=True, null=True)
    otros_cant = models.BooleanField(default=0)

    superficie_atendida_m2 = models.IntegerField(default=0)
    bancas_cemento = models.IntegerField(default=0)
    bancas_metalicas = models.IntegerField(default=0)
    multijuegos = models.IntegerField(default=0)
    resvaladeros = models.IntegerField(default=0)
    sube_baja = models.IntegerField(default=0)
    columpios = models.IntegerField(default=0)
    pasamanos = models.IntegerField(default=0)
    juego_esferas = models.IntegerField(default=0)
    canchas = models.IntegerField(default=0)
    porterias = models.IntegerField(default=0)
    encalado_arboles = models.IntegerField(default=0)
    levantado_malla = models.IntegerField(default=0)
    reposicion_malla = models.IntegerField(default=0)
    pintura_utilizada_litros = models.IntegerField(default=0)
    thinner_utilizado_litros = models.IntegerField(default=0)
    personal_trabajo = models.IntegerField(default=0)

    trabajo_realizado = models.TextField(blank=True, null=True)
    pendientes = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    colonia = models.CharField(max_length=100, blank=True)
    calle1 = models.CharField(max_length=100, blank=True)
    calle2 = models.CharField(max_length=100, blank=True)

    equipo_utilizado = models.TextField(blank=True, null=True)
    material_utilizado = models.TextField(blank=True, null=True)
    vehiculos_utilizados = models.TextField(blank=True, null=True)


class ReporteRiegoChamizal(models.Model):
    riego_en = models.CharField(max_length=100)
    fecha = models.DateField()
    dia = models.CharField(max_length=20, blank=True)
    encargado = models.CharField(max_length=100, blank=True)

    superficie_atendida_m2 = models.IntegerField(default=0)
    reparacion_fugas = models.IntegerField(default=0)
    limpieza_aspersores = models.IntegerField(default=0)
    basura_recolectada = models.IntegerField(default=0)
    papel_m2 = models.IntegerField(default=0)
    personal_trabajo = models.IntegerField(default=0)

    ubicacion_area = models.CharField(max_length=200, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

class ReporteRiegoPipas(models.Model):
    fecha = models.DateField()
    dia = models.CharField(max_length=20, blank=True)
    nombre_chofer = models.CharField(max_length=100, blank=True)
    nombre_ayudante = models.CharField(max_length=100, blank=True)
    engomado_vehiculo = models.CharField(max_length=100, blank=True)
    hora_salida = models.TimeField()
    hora_regreso = models.TimeField()
    lugar_riego = models.CharField(max_length=100, blank=True)

    colonia = models.CharField(max_length=100, blank=True)
    calle1 = models.CharField(max_length=100, blank=True)
    calle2 = models.CharField(max_length=100, blank=True)

    viajes = models.IntegerField(default=0)
    agua_empleada_litros = models.IntegerField(default=0)

    observaciones = models.TextField(blank=True, null=True)
