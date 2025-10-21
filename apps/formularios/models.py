from django.db import models

class ReporteCuadrilla(models.Model):
    folio_pac = models.IntegerField(blank=True, null=True)

    # Datos generales
    distrito = models.CharField(max_length=100)
    dia = models.CharField(max_length=20)
    fecha = models.DateField()

    trabajo_realizado = models.TextField()
    pendientes = models.TextField()

    coordinador = models.CharField(max_length=100)
    encargado_cuadrilla = models.CharField(max_length=100)

    # Áreas atendidas
    parques_comunitarios = models.BooleanField(default=False)
    parques_municipales = models.BooleanField(default=False)
    monumentos_atendidos = models.BooleanField(default=False)
    camellones_atendidos = models.BooleanField(default=False)
    apoyo_areas_gob = models.BooleanField(default=False)
    otros = models.CharField(max_length=20, blank=True, null=True)
    otros_cant = models.BooleanField(default=False)



    # Superficies y trabajos
    superficie_atendida_m2 = models.IntegerField()
    cesped_cortado_m2 = models.IntegerField()
    deshierbe_m2 = models.IntegerField()
    arboles_plantados = models.IntegerField()
    arboles_podados = models.IntegerField()
    arboles_retirados = models.IntegerField()
    zacate_basura_kilos = models.IntegerField()
    escombro_kilos = models.IntegerField()
    llantas_recolectadas = models.IntegerField()
    papeleo_m2 = models.IntegerField()
    personal_trabajo = models.IntegerField()

    #Recursos
    equipo_utilizado = models.TextField()
    material_utilizado = models.TextField()
    vehiculos_utilizados = models.TextField()

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

    # Ubicación
    ubicacion_area = models.CharField(max_length=200)
    colonia_camellon = models.CharField(max_length=200)
    calle = models.CharField(max_length=200)

    # Tipo de trabajo
    trabajo_diario = models.BooleanField(default=False)
    trabajo_ciudadania = models.BooleanField(default=False)
    operativo_especial = models.BooleanField(default=False)
    operativo_comentarios = models.CharField(max_length=140, blank=True)


    def __str__(self):
        return f"Reporte {self.numero_reporte} - {self.dia}"


class ReporteChamizal(models.Model):
    folio_pac = models.IntegerField(blank=True, null=True)


    distrito = models.CharField(max_length=100)
    fecha = models.DateField()
    dia = models.CharField(max_length=20, blank=True)

    trabajo_diario = models.BooleanField(default=False)
    trabajo_ciudadania = models.BooleanField(default=False)
    operativo_especial = models.BooleanField(default=False)
    operativo_comentarios = models.CharField(max_length=140, blank=True)


    coordinador = models.CharField(max_length=100)
    encargado_cuadrilla = models.CharField(max_length=100)

    parque_chamizal = models.BooleanField(default=False)
    hoyos = models.BooleanField(default=False)
    camellones = models.BooleanField(default=False)
    otros = models.CharField(max_length=20, blank=True, null=True)
    otros_bool = models.BooleanField(default=False)

    superficie_atendida_m2 = models.IntegerField()
    cesped_cortado_m2 = models.IntegerField()
    deshierbe_m2 = models.IntegerField()
    arboles_plantados = models.IntegerField()
    arboles_podados = models.IntegerField()
    arboles_retirados = models.IntegerField()
    zacate_basura_kilos = models.IntegerField()
    papeleo_m2 = models.IntegerField()
    personal_trabajo = models.IntegerField()

    trabajo_realizado = models.TextField()
    pendientes = models.TextField()
    observaciones = models.TextField()

    ubicacion_area = models.CharField()

    equipo_utilizado = models.TextField()
    material_utilizado = models.TextField()
    vehiculos_utilizados = models.TextField()

    def __str__(self):
        return f"Reporte Chamizal"

class ReporteCultura(models.Model):
    folio_pac = models.IntegerField()


    fecha = models.DateField()
    dia = models.CharField(max_length=20)
    encargado = models.CharField(max_length=100)
    lugar = models.CharField(max_length=100)

    personas_beneficiadas = models.IntegerField()
    escuela_atendida = models.CharField(max_length=100)
    maquiladora_atendida = models.CharField(max_length=100)
    platica_sustentabilidad = models.CharField(max_length=100)
    curso_poda = models.CharField(max_length=100)
    comite_parque = models.CharField(max_length=100)

    colonia = models.CharField(max_length=100)
    calle1 = models.CharField(max_length=100)
    calle2 = models.CharField(max_length=100)
    calle3 = models.CharField(max_length=100)
    calle4 = models.CharField(max_length=100)

    observaciones = models.TextField()
    responsable = models.CharField(max_length=100, blank=True)
    nombre_ciudadano = models.CharField(max_length=100, blank=True)

class ReporteFuentes(models.Model):
    folio_pac = models.IntegerField()


    fecha = models.DateField()
    dia = models.CharField(max_length=20)
    coordinador = models.CharField(max_length=100)
    encargado = models.CharField(max_length=100)
    superficie_atendida_m2 = models.IntegerField()
    limpieza_papeleo_m2 = models.IntegerField()
    reparacion_tuberia = models.IntegerField()
    basura_kg = models.IntegerField()

    reparacion_bomba = models.IntegerField()
    instalacion_bomba = models.IntegerField()
    personal_trabajo = models.IntegerField()

    colonia = models.CharField(max_length=100)
    calle1 = models.CharField(max_length=100)
    calle2 = models.CharField(max_length=100)
    observaciones = models.TextField()

class ReporteFugas(models.Model):
    folio_pac = models.IntegerField(blank=True, null=True)

    distrito = models.CharField(max_length=100)
    fecha = models.DateField()
    dia = models.CharField(max_length=20)

    trabajo_diario = models.BooleanField(default=False)
    trabajo_ciudadania = models.BooleanField(default=False)
    operativo_especial = models.BooleanField(default=False)
    operativo_comentarios = models.CharField(max_length=140, blank=True)

    coordinador = models.CharField(max_length=100)
    encargado_cuadrilla = models.CharField(max_length=100)

    parques_comunitarios = models.BooleanField(default=False)
    parques_municipales = models.BooleanField(default=False)
    monumentos_atendidos = models.BooleanField(default=False)
    camellones_atendidos = models.BooleanField(default=False)
    apoyo_areas_gob = models.BooleanField(default=False)
    otros = models.CharField(max_length=20, blank=True, null=True)
    otros_cant = models.BooleanField(default=False)

    superficie_atendida_m2 = models.IntegerField()
    reparacion_fugas = models.IntegerField()
    instalacion_agua = models.IntegerField()
    instalacion_riego = models.IntegerField()
    revision_riego = models.IntegerField()
    material_riego = models.IntegerField()
    personal_trabajo = models.IntegerField()

    trabajo_realizado = models.TextField()
    pendientes = models.TextField()
    observaciones = models.TextField()

    colonia = models.CharField(max_length=100)
    calle1 = models.CharField(max_length=100)
    calle2 = models.CharField(max_length=100)

    equipo_utilizado = models.TextField()
    material_utilizado = models.TextField()
    vehiculos_utilizados = models.TextField()

class ReportePintura(models.Model):
    folio_pac = models.IntegerField(blank=True, null=True)


    fecha = models.DateField()
    dia = models.CharField(max_length=20)
    distrito = models.CharField(max_length=100)
    encargado = models.CharField(max_length=100)
    coordinador = models.CharField(max_length=100)

    trabajo_diario = models.BooleanField(default=False)
    trabajo_ciudadania = models.BooleanField(default=False)
    operativo_especial = models.BooleanField(default=False)
    operativo_comentarios = models.CharField(max_length=140, blank=True)

    comunitarios_atendidos = models.BooleanField(default=False)
    municipales_atendidos = models.BooleanField(default=False)
    monumentos_atendidos = models.BooleanField(default=False)
    camellones_atendidos = models.BooleanField(default=False)
    apoyo_areas_gob = models.BooleanField(default=False)
    otros = models.CharField(max_length=20, blank=True, null=True)
    otros_cant = models.BooleanField(default=False)

    superficie_atendida_m2 = models.IntegerField()
    bancas_cemento = models.IntegerField()
    bancas_metalicas = models.IntegerField()
    multijuegos = models.IntegerField()
    resvaladeros = models.IntegerField()
    sube_baja = models.IntegerField()
    columpios = models.IntegerField()
    pasamanos = models.IntegerField()
    juego_esferas = models.IntegerField()
    canchas = models.IntegerField()
    porterias = models.IntegerField()
    encalado_arboles = models.IntegerField()
    levantado_malla = models.IntegerField()
    reposicion_malla = models.IntegerField()
    pintura_utilizada_litros = models.IntegerField()
    thinner_utilizado_litros = models.IntegerField()
    personal_trabajo = models.IntegerField()

    trabajo_realizado = models.TextField()
    pendientes = models.TextField()
    observaciones = models.TextField()

    colonia = models.CharField(max_length=100)
    calle1 = models.CharField(max_length=100)
    calle2 = models.CharField(max_length=100)

    equipo_utilizado = models.TextField()
    material_utilizado = models.TextField()
    vehiculos_utilizados = models.TextField()


class ReporteRiegoChamizal(models.Model):
    folio_pac = models.IntegerField(blank=True, null=True)


    riego_en = models.CharField(max_length=100)
    fecha = models.DateField()
    dia = models.CharField(max_length=20)
    encargado = models.CharField(max_length=100)

    superficie_atendida_m2 = models.IntegerField()
    reparacion_fugas = models.IntegerField()
    limpieza_aspersores = models.IntegerField()
    basura_recolectada = models.IntegerField()
    papel_m2 = models.IntegerField()
    personal_trabajo = models.IntegerField()

    ubicacion_area = models.CharField(max_length=200)
    observaciones = models.TextField()

class ReporteRiegoPipas(models.Model):
    folio_pac = models.IntegerField()


    fecha = models.DateField()
    dia = models.CharField(max_length=20)
    nombre_chofer = models.CharField(max_length=100)
    nombre_ayudante = models.CharField(max_length=100)
    engomado_vehiculo = models.CharField(max_length=100)
    hora_salida = models.TimeField()
    hora_regreso = models.TimeField()
    lugar_riego = models.CharField(max_length=100)

    colonia = models.CharField(max_length=100)
    calle1 = models.CharField(max_length=100)
    calle2 = models.CharField(max_length=100)

    viajes = models.IntegerField()
    agua_empleada_litros = models.IntegerField()

    observaciones = models.TextField()
