from django import forms
from .models import *

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
            "trabajo_diario": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "trabajo_ciudadania": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "operativo_especial": forms.CheckboxInput(attrs={"class": "form-check-input"}),

            # Selected
            "dia": forms.Select(
                choices=[
                    ("lunes", "Lunes"),
                    ("martes", "Martes"),
                    ("miércoles", "Miércoles"),
                    ("jueves", "Jueves"),
                    ("viernes", "Viernes"),
                    ("sábado", "Sábado"),
                    ("domingo", "Domingo"),
                ],
                attrs={"class": "form-select form-control"}
            ),

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
            "dia": forms.Select(
                choices=[
                    ("lunes", "Lunes"),
                    ("martes", "Martes"),
                    ("miércoles", "Miércoles"),
                    ("jueves", "Jueves"),
                    ("viernes", "Viernes"),
                    ("sábado", "Sábado"),
                    ("domingo", "Domingo"),
                ],
                attrs={"class": "form-select form-control"}
            ),

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


class ReporteCulturaForm(FormControlMixin, forms.ModelForm):
    numero_reporte = forms.IntegerField(label="Número de Reporte", required=False, disabled=True)
    class Meta:
        model = ReporteCultura
        fields = "__all__"
        widgets = {
            "fecha": forms.DateInput(attrs={"type": "date"}),
            "observaciones": forms.Textarea(attrs={"rows": 8}),

            # Selected
            "dia": forms.Select(
                choices=[
                    ("lunes", "Lunes"),
                    ("martes", "Martes"),
                    ("miércoles", "Miércoles"),
                    ("jueves", "Jueves"),
                    ("viernes", "Viernes"),
                    ("sábado", "Sábado"),
                    ("domingo", "Domingo"),
                ],
                attrs={"class": "form-select form-control"}
            ),
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
            "dia": forms.Select(
                choices=[
                    ("lunes", "Lunes"),
                    ("martes", "Martes"),
                    ("miércoles", "Miércoles"),
                    ("jueves", "Jueves"),
                    ("viernes", "Viernes"),
                    ("sábado", "Sábado"),
                    ("domingo", "Domingo"),
                ],
                attrs={"class": "form-select form-control"}
            ),

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
            "dia": forms.Select(
                choices=[
                    ("lunes", "Lunes"),
                    ("martes", "Martes"),
                    ("miércoles", "Miércoles"),
                    ("jueves", "Jueves"),
                    ("viernes", "Viernes"),
                    ("sábado", "Sábado"),
                    ("domingo", "Domingo"),
                ],
                attrs={"class": "form-select form-control"}
            ),

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
            "dia": forms.Select(
                choices=[
                    ("lunes", "Lunes"),
                    ("martes", "Martes"),
                    ("miércoles", "Miércoles"),
                    ("jueves", "Jueves"),
                    ("viernes", "Viernes"),
                    ("sábado", "Sábado"),
                    ("domingo", "Domingo"),
                ],
                attrs={"class": "form-select form-control"}
            ),

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


class ReporteRiegoChamizalForm(FormControlMixin, forms.ModelForm):
    numero_reporte = forms.IntegerField(label="Número de Reporte", required=False, disabled=True)

    class Meta:
        model = ReporteRiegoChamizal
        fields = "__all__"
        widgets = {
            "fecha": forms.DateInput(attrs={"type": "date"}),

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
            "dia": forms.Select(
                choices=[
                    ("lunes", "Lunes"),
                    ("martes", "Martes"),
                    ("miércoles", "Miércoles"),
                    ("jueves", "Jueves"),
                    ("viernes", "Viernes"),
                    ("sábado", "Sábado"),
                    ("domingo", "Domingo"),
                ],
                attrs={"class": "form-select form-control"}
            ),
        }