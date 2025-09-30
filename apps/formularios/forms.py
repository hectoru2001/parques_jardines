from django import forms
from .models import *


DIAS_SEMANA = [
    ("lunes", "Lunes"),
    ("martes", "Martes"),
    ("miércoles", "Miércoles"),
    ("jueves", "Jueves"),
    ("viernes", "Viernes"),
    ("sábado", "Sábado"),
    ("domingo", "Domingo"),
]

DISTRITOS = [
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
]


# Estilo de formularios con Bootstrap
class FormControlMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, (forms.CheckboxInput, forms.RadioSelect)):
                css_class = field.widget.attrs.get("class", "")
                if "form-control" not in css_class:
                    field.widget.attrs["class"] = (css_class + " form-control").strip()

class ReporteCuadrillaForm(FormControlMixin,forms.ModelForm):
    numero_reporte = forms.IntegerField(label="Número de Reporte", required=False, disabled=True)
    class Meta:
        model = ReporteCuadrilla
        fields = "__all__"
        widgets = {
            "fecha": forms.DateInput(attrs={"type": "date"}),
            "observaciones_parque": forms.Textarea(attrs={"rows": 3}),
            "otras_observaciones": forms.Textarea(attrs={"rows": 3}),
            "pendientes": forms.Textarea(attrs={"rows": 3}),
            "equipo_utilizado": forms.Textarea(attrs={"rows": 2}),
            "material_utilizado": forms.Textarea(attrs={"rows": 2}),
            "vehiculos_utilizados": forms.Textarea(attrs={"rows": 2}),

            # Checkboxes
            "trabajo_diario": forms.CheckboxInput(attrs={"class": "form-check-input tipo-trabajo"}),
            "trabajo_ciudadania": forms.CheckboxInput(attrs={"class": "form-check-input tipo-trabajo"}),
            "operativo_especial": forms.CheckboxInput(attrs={"class": "form-check-input tipo-trabajo"}),

            # Selected
            "dia": forms.Select(choices=DIAS_SEMANA, attrs={"class": "form-select form-control"}),
            "distrito": forms.Select(choices=DISTRITOS, attrs={"class": "form-select form-control"}),

            # Radio Select
            "pintura_juegos": forms.RadioSelect,
            "cuenta_alumbrado": forms.RadioSelect,
            "cuenta_jueguitos": forms.RadioSelect,
            "cuenta_mobiliario": forms.RadioSelect,
            "cuenta_sistema_riego": forms.RadioSelect,
            "necesita_reforestacion": forms.RadioSelect,

            # Dropdown
            "frecuencia_recoleccion_basura": forms.Select,
        }
        labels = {
            "dia": "Día",
            "trabajo_ciudadania": "Trabajo de la ciudadanía",
            "superficie_atendida_m2": "Superficie atendida (m²)",
            "apoyo_areas_gob": "Apoyo a áreas de gobierno",
            "cesped_cortado_m2": "Césped cortado (m²)",
            "deshierbe_m2": "Deshierbe (m²)",
            "arboles_plantados": "Árboles plantados (Num)",
            "arboles_podados": "Árbooles podados (Num)",
            "arboles_retirados": "Árboles retirados (Num)",
            "zacate_basura_kilos": "Zacate, basura y ramas recolectadas (kilos)",
            "escombro_kilos": "Escombro o tierra de arrastre (kilos)",
            "llantas_recolectadas": "Llantas recolectadas (Num)",
            "papeleo_m2": "Papeleo (m²)",
            "personal_trabajo": "Personal que trabajo (Num)",

            "colonia_camellon" : "Colonia o Camellón",
            "ubicacion_area" : "Ubicación o Área",
            "trabajo_ciudadania" : "Trabajo de la ciudadanía",
        
            "vehiculos_utilizados": "Vehículos utilizados",
        }


class ReporteChamizalForm(FormControlMixin, forms.ModelForm):
    numero_reporte = forms.IntegerField(label="Número de Reporte", required=False, disabled=True)
    class Meta:
        model = ReporteChamizal
        fields = "__all__"
        widgets = {
            "fecha": forms.DateInput(attrs={"type": "date"}),
            "observaciones": forms.Textarea(attrs={"rows": 5}),
            "otras_observaciones": forms.Textarea(attrs={"rows": 3}),
            "pendientes": forms.Textarea(attrs={"rows": 3}),
            "equipo_utilizado": forms.Textarea(attrs={"rows": 2}),
            "material_utilizado": forms.Textarea(attrs={"rows": 2}),
            "vehiculos_utilizados": forms.Textarea(attrs={"rows": 2}),

            # Checkboxes
            "trabajo_diario": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "trabajo_ciudadania": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "operativo_especial": forms.CheckboxInput(attrs={"class": "form-check-input"}),

            # Selected
            "dia": forms.Select(choices=DIAS_SEMANA, attrs={"class": "form-select form-control"}),
            "distrito": forms.Select(choices=DISTRITOS, attrs={"class": "form-select form-control"}),

            # Radio Select
            "pintura_juegos": forms.RadioSelect,
            "cuenta_alumbrado": forms.RadioSelect,
            "cuenta_jueguitos": forms.RadioSelect,
            "cuenta_mobiliario": forms.RadioSelect,
            "cuenta_sistema_riego": forms.RadioSelect,
            "necesita_reforestacion": forms.RadioSelect,

            # Dropdown
            "frecuencia_recoleccion_basura": forms.Select,

        
        }
        labels = {
        
            "dia": "Día",
            "trabajo_ciudadania": "Trabajo de la ciudadanía",

            "superficie_atendida_m2": "Superficie atendida (m²)",
            "cesped_cortado_m2": "Césped cortado (m²)",
            "deshierbe_m2": "Deshierbe (m²)",
            "arboles_plantados": "Árboles plantados (Num)",
            "arboles_podados": "Árbooles podados (Num)",
            "arboles_retirados": "Árboles retirados (Num)",
            "zacate_basura_kilos": "Zacate, basura y ramas recolectadas (kilos)",
            "papeleo_m2": "Papeleo (m²)",
            "personal_trabajo": "Personal que trabajo (Num)",

            "ubicacion_area" : "Ubicación o Área",
            "vehiculos_utilizados": "Vehículos utilizados",
        }


class ReporteCulturaForm(FormControlMixin, forms.ModelForm):
    numero_reporte = forms.IntegerField(label="Número de Reporte", required=False, disabled=True)
    class Meta:
        model = ReporteCultura
        fields = "__all__"
        widgets = {
            "fecha": forms.DateInput(attrs={"type": "date"}),
            "observaciones": forms.Textarea(attrs={"rows": 8}),

            # Selected
            "dia": forms.Select(choices=DIAS_SEMANA, attrs={"class": "form-select form-control"}),

        }
        labels = {
            "dia": "Día",
            "comite_parque": "Comité de vecinos / Parque atendido",
            "calle1": "Calle 1",
            "calle2": "Calle 2",
            "calle3": "Calle 3",
            "calle4": "Calle 4",
        }



class ReporteFuentesForm(FormControlMixin, forms.ModelForm):
    numero_reporte = forms.IntegerField(label="Número de Reporte", required=False, disabled=True)

    class Meta:
        model = ReporteFuentes
        fields = "__all__"
        widgets = {
            "fecha": forms.DateInput(attrs={"type": "date"}),
            "observaciones": forms.Textarea(attrs={"rows": 5}),
            "otras_observaciones": forms.Textarea(attrs={"rows": 3}),
            "pendientes": forms.Textarea(attrs={"rows": 3}),
            "equipo_utilizado": forms.Textarea(attrs={"rows": 2}),
            "material_utilizado": forms.Textarea(attrs={"rows": 2}),
            "vehiculos_utilizados": forms.Textarea(attrs={"rows": 2}),

            # Checkboxes
            "trabajo_diario": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "trabajo_ciudadania": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "operativo_especial": forms.CheckboxInput(attrs={"class": "form-check-input"}),

            # Selected
            "dia": forms.Select(choices=DIAS_SEMANA, attrs={"class": "form-select form-control"}),

            # Radio Select
            "pintura_juegos": forms.RadioSelect,
            "cuenta_alumbrado": forms.RadioSelect,
            "cuenta_jueguitos": forms.RadioSelect,
            "cuenta_mobiliario": forms.RadioSelect,
            "cuenta_sistema_riego": forms.RadioSelect,
            "necesita_reforestacion": forms.RadioSelect,

            # Dropdown
            "frecuencia_recoleccion_basura": forms.Select,
        }
        labels = {
            "dia": "Día",
            "superficie_atendida_m2": "Superficie atendida (m²)",
            "limpieza_papeleo_m2": "Limpieza de papeleo (m²)",
            "reparacion_tuberia" : "Reparación de tubería (Num)",
            "basura_kg": "Basura recolectada (kilos)",

            "reparacion_bomba" : "Reparación de bomba (Num)",
            "instalacion_bomba" : "Instalación de bomba (Num)",
            "personal_trabajo": "Personal que trabajo (Num)",

            "calle1" : "Calle 1",
            "calle2" : "Calle 2",
        }


class ReporteFugasForm(FormControlMixin, forms.ModelForm):
    numero_reporte = forms.IntegerField(label="Número de Reporte", required=False, disabled=True)

    class Meta:
        model = ReporteFugas
        fields = "__all__"
        widgets = {
            "fecha": forms.DateInput(attrs={"type": "date"}),
            "observaciones": forms.Textarea(attrs={"rows": 5}),
            "otras_observaciones": forms.Textarea(attrs={"rows": 3}),
            "pendientes": forms.Textarea(attrs={"rows": 3}),
            "equipo_utilizado": forms.Textarea(attrs={"rows": 2}),
            "material_utilizado": forms.Textarea(attrs={"rows": 2}),
            "vehiculos_utilizados": forms.Textarea(attrs={"rows": 2}),

            # Checkboxes
            "trabajo_diario": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "trabajo_ciudadania": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "operativo_especial": forms.CheckboxInput(attrs={"class": "form-check-input"}),

            # Selected
            "dia": forms.Select(choices=DIAS_SEMANA, attrs={"class": "form-select form-control"}),
            "distrito": forms.Select(choices=DISTRITOS, attrs={"class": "form-select form-control"}),         

            # Radio Select
            "pintura_juegos": forms.RadioSelect,
            "cuenta_alumbrado": forms.RadioSelect,
            "cuenta_jueguitos": forms.RadioSelect,
            "cuenta_mobiliario": forms.RadioSelect,
            "cuenta_sistema_riego": forms.RadioSelect,
            "necesita_reforestacion": forms.RadioSelect,

            # Dropdown
            "frecuencia_recoleccion_basura": forms.Select,
        }

        labels = {
            "dia": "Día",
            "trabajo_ciudadania": "Trabajo de la ciudadanía",
            "apoyo_areas_gob": "Apoyo a áreas de gobierno",

            "superficie_atendida_m2": "Superficie atendida (m²)",
            "reparacion_fugas": "Reparación de fuga (Num)",
            "instalacion_agua": "Instalación de toma de agua (Num)",
            "instalacion_riego": "Instalación de sistema de riego (Num)",
            "revision_riego": "Revisión y reparación de sistema de riego (Num)",
            "material_riego": "Listado de material para sistema de riego (Num)",
            "personal_trabajo": "Personal que trabajo (Num)",

            "colonia": "Colonia o Camellón",
            "calle1": "Calle 1",
            "calle2": "Calle 2",

            "vehiculos_utilizados": "Vehículos utilizados",
        }


class ReportePinturasForm(FormControlMixin, forms.ModelForm):
    numero_reporte = forms.IntegerField(label="Número de Reporte", required=False, disabled=True)

    class Meta:
        model = ReportePintura
        fields = "__all__"
        widgets = {
            "fecha": forms.DateInput(attrs={"type": "date"}),
            "observaciones": forms.Textarea(attrs={"rows": 5}),
            "otras_observaciones": forms.Textarea(attrs={"rows": 3}),
            "pendientes": forms.Textarea(attrs={"rows": 3}),
            "equipo_utilizado": forms.Textarea(attrs={"rows": 2}),
            "material_utilizado": forms.Textarea(attrs={"rows": 2}),
            "vehiculos_utilizados": forms.Textarea(attrs={"rows": 2}),

            # Checkboxes
            "trabajo_diario": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "trabajo_ciudadania": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "operativo_especial": forms.CheckboxInput(attrs={"class": "form-check-input"}),

            # Selected
            "dia": forms.Select(choices=DIAS_SEMANA, attrs={"class": "form-select form-control"}),
            "distrito": forms.Select(choices=DISTRITOS, attrs={"class": "form-select form-control"}),

            # Radio Select
            "pintura_juegos": forms.RadioSelect,
            "cuenta_alumbrado": forms.RadioSelect,
            "cuenta_jueguitos": forms.RadioSelect,
            "cuenta_mobiliario": forms.RadioSelect,
            "cuenta_sistema_riego": forms.RadioSelect,
            "necesita_reforestacion": forms.RadioSelect,

            # Dropdown
            "frecuencia_recoleccion_basura": forms.Select,
        }
        labels = {
            "dia": "Día",
            "trabajo_ciudadania": "Trabajo de la ciudadanía",
            "apoyo_areas_gob": "Apoyo a áreas verdes de gobierno",

            "superficie_atendida_m2": "Superficie atendida (m²)",
            "bancas_cemento": "Bancas de cemento (Num)",
            "bancas_metalicas": "Bancas metálicas (Num)",
            "multijuegos": "Multijuegos (Num)",
            "resvaladeros": "Resbaladero (Num)",
            "sube_baja": "Sube y baja (Num)",
            "columpios": "Columpios (Num)",
            "pasamanos": "Pasamanos (Num)",
            "juego_esferas": "Juego de esferas (Num)",
            "canchas": "Canchas (Num)",
            "porterias": "Porterías (Num)",
            "encalado_arboles": "Encalado de árboles (Num)",
            "levantado_malla": "Levantamiento de malla ciclónica (Num)",
            "reposicion_malla": "Reposición de malla ciclónica (Num)",
            "pintura_utilizada_litros": "Pintura utilizada (Litros)",
            "thinner_utilizado_litros": "Thinner utilizado (Litros)",
            "personal_trabajo": "Personal que trabajo (Num)",

            "colonia": "Colonia o Camellón",
            "calle1": "Calle 1",
            "calle2": "Calle 2",

            "vehiculos_utilizados": "Vehículos utilizados",
        }


class ReporteRiegoChamizalForm(FormControlMixin, forms.ModelForm):
    numero_reporte = forms.IntegerField(label="Número de Reporte", required=False, disabled=True)

    class Meta:
        model = ReporteRiegoChamizal
        fields = "__all__"
        widgets = {
            "fecha": forms.DateInput(attrs={"type": "date"}),
            "dia": forms.Select(choices=DIAS_SEMANA, attrs={"class": "form-select form-control"}),


        }
        labels = {
            "dia": "Día",

            "superficie_atendida_m2": "Superficie atendida (m²)",
            "reparacion_fugas": "Reparación de fuga (Num)",
            "limpieza_aspersores": "Limpieza de aspersores (Num)",
            "basura_recolectada": "Basura recolectada (kg)",
            "papel_m2": "Papeleo (m²)",
            "personal_trabajo": "Personal que trabajo (Num)",

            "ubicacion_area": "Ubicación del área trabajada",   
        }

class ReporteRiegoPipasForm(FormControlMixin, forms.ModelForm):
    numero_reporte = forms.IntegerField(label="Número de Reporte", required=False, disabled=True)

    class Meta:
        model = ReporteRiegoPipas
        fields = "__all__"
        widgets = {
            "fecha": forms.DateInput(attrs={"type": "date"}),
            "hora_salida": forms.TimeInput(attrs={"type": "time"}),
            "hora_regreso": forms.TimeInput(attrs={"type": "time"}),
            "dia": forms.Select(choices=DIAS_SEMANA, attrs={"class": "form-select form-control"}),
        }
        labels = {
            "dia": "Día",

            "engomado_vehiculo": "Engomado del vehículo",
            "hora_salida": "Hora de salida",
            "hora_regreso": "Hora de regreso",
            "lugar_riego": "Lugar de riego",

            "colonia": "Colonia o AV. Principal",
            "calle1": "Calle 1",
            "calle2": "Calle 2",

            "agua_empleada_litros": "Agua empleada (Litros)",
        }