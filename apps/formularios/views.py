from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from .models import *
from django.db.models import Max
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import JsonResponse
import json
import fitz  # PyMuPDF
from io import BytesIO
from .decoradores import requiere_grupo, es_capturista



@login_required
def plantilla(request):
    total_reportes = ReporteCuadrilla.objects.count()
    reportes_hoy = ReporteCuadrilla.objects.filter(fecha=timezone.now().date()).count()
    reportes_pendientes = ReporteCuadrilla.objects.filter(pendientes__isnull=False).count()
    ultimos_reportes = ReporteCuadrilla.objects.order_by('-id')[:5]

    return render(request, "contenido.html", {
        "total_reportes": total_reportes,
        "reportes_hoy": reportes_hoy,
        "reportes_pendientes": reportes_pendientes,
        "ultimos_reportes": ultimos_reportes
    })

def menu_botones(request):
    return render(request, "main.html")


# ===================== Generar nuevo reporte =====================
@login_required
@requiere_grupo("Reporte Cuadrilla")
def formato_cuadrilla(request):
    last = ReporteCuadrilla.objects.aggregate(Max('id'))['id__max']
    siguiente_id = 1 if not last else last + 1

    if request.method == "POST":
        form = ReporteCuadrillaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_cuadrillas")
        else:
            print(form.errors)
    else:
        form = ReporteCuadrillaForm()
        form.fields['numero_reporte'].initial = siguiente_id

    return render(request, "formularios/cuadrilla.html", {"form": form, "siguiente_id": siguiente_id})

@login_required
@requiere_grupo("Reporte Chamizal")
def formato_chamizal(request):
    last = ReporteChamizal.objects.aggregate(Max('id'))['id__max']
    siguiente_id = 1 if not last else last + 1

    if request.method == "POST":
        form = ReporteChamizalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_chamizal")
        else:
            print(form.errors)
    else:
        form = ReporteChamizalForm()
        form.fields['numero_reporte'].initial = siguiente_id

    return render(request, "formularios/chamizal.html", {"form": form, "siguiente_id": siguiente_id})

@login_required
@requiere_grupo("Reporte Cultura")
def formato_cultura(request):
    last = ReporteCultura.objects.aggregate(Max('id'))['id__max']
    siguiente_id = 1 if not last else last + 1

    if request.method == "POST":
        form = ReporteCulturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_cultura")
        else:
            print(form.errors)
    else:
        form = ReporteCulturaForm()
        form.fields['numero_reporte'].initial = siguiente_id

    return render(request, "formularios/cultura.html", {"form": form, "siguiente_id": siguiente_id})

@login_required
@requiere_grupo("Reporte Fuentes")
def formato_fuentes(request):
    last = ReporteFuentes.objects.aggregate(Max('id'))['id__max']
    siguiente_id = 1 if not last else last + 1

    if request.method == "POST":
        form = ReporteFuentesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_fuentes")
        else:
            print(form.errors)
    else:
        form = ReporteFuentesForm()
        form.fields['numero_reporte'].initial = siguiente_id

    return render(request, "formularios/fuentes.html", {"form": form, "siguiente_id": siguiente_id})

@login_required
@requiere_grupo("Reporte Fugas")
def formato_fugas(request):
    last = ReporteFugas.objects.aggregate(Max('id'))['id__max']
    siguiente_id = 1 if not last else last + 1

    if request.method == "POST":
        form = ReporteFugasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_fugas")
        else:
            print(form.errors)
    else:
        form = ReporteFugasForm()
        form.fields['numero_reporte'].initial = siguiente_id

    return render(request, "formularios/fugas.html", {"form": form, "siguiente_id": siguiente_id})

@login_required
@requiere_grupo("Reporte Pintura")
def formato_pinturas(request):
    last = ReportePintura.objects.aggregate(Max('id'))['id__max']
    siguiente_id = 1 if not last else last + 1

    if request.method == "POST":
        form = ReportePinturasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_pinturas")
        else:
            print(form.errors)
    else:
        form = ReportePinturasForm()
        form.fields['numero_reporte'].initial = siguiente_id

    return render(request, "formularios/pintura.html", {"form": form, "siguiente_id": siguiente_id})

@login_required
@requiere_grupo("Riego Chamizal")
def formato_riego_chamizal(request):
    last = ReporteRiegoChamizal.objects.aggregate(Max('id'))['id__max']
    siguiente_id = 1 if not last else last + 1

    if request.method == "POST":
        form = ReporteRiegoChamizalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_riego_chamizal")
        else:
            print(form.errors)
    else:
        form = ReporteRiegoChamizalForm()
        form.fields['numero_reporte'].initial = siguiente_id

    return render(request, "formularios/riego_chamizal.html", {"form": form, "siguiente_id": siguiente_id})

@login_required
@requiere_grupo("Riego Chamizal")
def formato_riego_pipas(request):
    last = ReporteRiegoChamizal.objects.aggregate(Max('id'))['id__max']
    siguiente_id = 1 if not last else last + 1

    if request.method == "POST":
        form = ReporteRiegoPipasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_riego_pipas")
        else:
            print(form.errors)
    else:
        form = ReporteRiegoPipasForm()
        form.fields['numero_reporte'].initial = siguiente_id

    return render(request, "formularios/riego_pipa.html", {"form": form, "siguiente_id": siguiente_id})

@login_required
@requiere_grupo("Soldadura")
def formato_soldadura(request):
    if request.method == 'POST':
        form = ReporteSoldaduraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.succes("Reporte generado correctamente")
            return redirect("lista_soldadura")
        else:
            print(form.errors)
        
    else:
        form = ReporteSoldaduraForm()

    return render(request, "formularios/soldadura.html", {"form": form})


# ===================== Cargar listado de reportes =====================
@login_required
@requiere_grupo("Reporte Cuadrilla")
def lista_cuadrilla(request):
    id = request.GET.get("id")
    if id:
        reportes = ReporteCuadrilla.objects.filter(id=id).order_by('-fecha')
    else:
        reportes = ReporteCuadrilla.objects.all().order_by('-fecha')

    return render(request, "gestion/lista_cuadrillas.html", {
        "reportes": reportes,
        "id": id
    })


@login_required
@requiere_grupo("Reporte Chamizal")
def lista_chamizal(request):
    id = request.GET.get("id")
    if id:
        reportes = ReporteChamizal.objects.filter(id=id).order_by('-fecha')
    else:
        reportes = ReporteChamizal.objects.all().order_by('-fecha')

    return render(request, "gestion/lista_chamizal.html", {
        "reportes": reportes,
        "id": id
    })

@login_required
@requiere_grupo("Reporte Cultura")
def lista_cultura(request):
    id = request.GET.get("id")
    if id:
        reportes = ReporteCultura.objects.filter(id=id).order_by('-fecha')
    else:
        reportes = ReporteCultura.objects.all().order_by('-fecha')

    return render(request, "gestion/lista_cultura.html", {
        "reportes": reportes,
        "id": id
    })

@login_required
@requiere_grupo("Reporte Fuentes")
def lista_fuentes(request):
    id = request.GET.get("id")
    if id:
        reportes = ReporteFuentes.objects.filter(id=id).order_by('-fecha')
    else:
        reportes = ReporteFuentes.objects.all().order_by('-fecha')

    return render(request, "gestion/lista_fuentes.html", {
        "reportes": reportes,
        "id": id
    })

@login_required
@requiere_grupo("Reporte Fugas")
def lista_fugas(request):
    id = request.GET.get("id")
    if id:
        reportes = ReporteFugas.objects.filter(id=id).order_by('-fecha')
    else:
        reportes = ReporteFugas.objects.all().order_by('-fecha')

    return render(request, "gestion/lista_fugas.html", {
        "reportes": reportes,
        "id": id
    })

@login_required
@requiere_grupo("Reporte Pintura")
def lista_pintura(request):
    id = request.GET.get("id")
    if id:
        reportes = ReportePintura.objects.filter(id=id).order_by('-fecha')
    else:
        reportes = ReportePintura.objects.all().order_by('-fecha')

    return render(request, "gestion/lista_pinturas.html", {
        "reportes": reportes,
        "id": id
    })

@login_required
@requiere_grupo("Riego Chamizal")
def lista_riego_chamizal(request):
    id = request.GET.get("id")
    if id:
        reportes = ReporteRiegoChamizal.objects.filter(id=id).order_by('-fecha')
    else:
        reportes = ReporteRiegoChamizal.objects.all().order_by('-fecha')

    return render(request, "gestion/lista_riego_chamizal.html", {
        "reportes": reportes,
        "id": id
    })

@login_required
@requiere_grupo("Riego Pipas")
def lista_riego_pipas(request):
    id = request.GET.get("id")
    if id:
        reportes = ReporteRiegoPipas.objects.filter(id=id).order_by('-fecha')
    else:
        reportes = ReporteRiegoPipas.objects.all().order_by('-fecha')

    return render(request, "gestion/lista_riego_pipa.html", {
        "reportes": reportes,
        "id": id
    })

@login_required
@requiere_grupo("Soldadura")
def lista_soldadura(request):
    id = request.GET.get("id")
    if id:
        reportes = ReporteSoldadura.objects.filter(id=id).order_by('-fecha')
    else:
        reportes = ReporteSoldadura.objects.all().order_by('-fecha')

    return render(request, "gestion/lista_soldadura.html", {
        "reportes": reportes,
        "id": id
    })

# ===================== Edición de reportes =====================
@login_required
@requiere_grupo("Reporte Cuadrilla")
@es_capturista
def formato_cuadrilla_editar(request, pk):
    reporte = get_object_or_404(ReporteCuadrilla, id=pk)

    if request.method == "POST":
        form = ReporteCuadrillaForm(request.POST, instance=reporte)
        if form.is_valid():
            form.save()
            return redirect("lista_cuadrillas")
    else:
        form = ReporteCuadrillaForm(instance=reporte)

    return render(request, "formularios/cuadrilla.html", {"form": form, "numero_reporte":pk})

@login_required
@requiere_grupo("Reporte Chamizal")
@es_capturista
def formato_chamizal_editar(request, pk):
    reporte = get_object_or_404(ReporteChamizal, id=pk)

    if request.method == "POST":
        form = ReporteChamizalForm(request.POST, instance=reporte)
        if form.is_valid():
            form.save()
            return redirect("lista_chamizal")
    else:
        form = ReporteChamizalForm(instance=reporte)

    return render(request, "formularios/chamizal.html", {"form": form, "numero_reporte":pk})

@login_required
@requiere_grupo("Reporte Cultura")
@es_capturista
def formato_cultura_editar(request, pk):
    reporte = get_object_or_404(ReporteCultura, id=pk)

    if request.method == "POST":
        form = ReporteCulturaForm(request.POST, instance=reporte)
        if form.is_valid():
            form.save()
            return redirect("lista_cultura")
    else:
        form = ReporteCulturaForm(instance=reporte)

    return render(request, "formularios/cultura.html", {"form": form, "numero_reporte":pk})

@login_required
@requiere_grupo("Reporte Fuentes")
@es_capturista
def formato_fuentes_editar(request, pk):
    reporte = get_object_or_404(ReporteFuentes, id=pk)

    if request.method == "POST":
        form = ReporteFuentesForm(request.POST, instance=reporte)
        if form.is_valid():
            form.save()
            return redirect("lista_fuentes")
    else:
        form = ReporteFuentesForm(instance=reporte)

    return render(request, "formularios/fuentes.html", {"form": form, "numero_reporte":pk})

@login_required
@requiere_grupo("Reporte Fugas")
@es_capturista
def formato_fugas_editar(request, pk):
    reporte = get_object_or_404(ReporteFugas, id=pk)

    if request.method == "POST":
        form = ReporteFugasForm(request.POST, instance=reporte)
        if form.is_valid():
            form.save()
            return redirect("lista_fugas")
    else:
        form = ReporteFugasForm(instance=reporte)

    return render(request, "formularios/fugas.html", {"form": form, "numero_reporte":pk})

@login_required
@requiere_grupo("Reporte Pintura")
@es_capturista
def formato_pinturas_editar(request, pk):
    reporte = get_object_or_404(ReportePintura, id=pk)

    if request.method == "POST":
        form = ReportePinturasForm(request.POST, instance=reporte)
        if form.is_valid():
            form.save()
            return redirect("lista_pinturas")
    else:
        form = ReportePinturasForm(instance=reporte)

    return render(request, "formularios/pintura.html", {"form": form, "numero_reporte":pk})

@login_required
@requiere_grupo("Riego Chamizal")
@es_capturista
def formato_riego_chamizal_editar(request, pk):
    reporte = get_object_or_404(ReporteRiegoChamizal, id=pk)

    if request.method == "POST":
        form = ReporteRiegoChamizalForm(request.POST, instance=reporte)
        if form.is_valid():
            form.save()
            return redirect("lista_riego_chamizal")
    else:
        form = ReporteRiegoChamizalForm(instance=reporte)

    return render(request, "formularios/riego_chamizal.html", {"form": form, "numero_reporte":pk})

@login_required
@requiere_grupo("Riego Pipas")
@es_capturista
def formato_riego_pipas_editar(request, pk):
    reporte = get_object_or_404(ReporteRiegoPipas, id=pk)

    if request.method == "POST":
        form = ReporteRiegoPipasForm(request.POST, instance=reporte)
        if form.is_valid():
            form.save()
            return redirect("lista_riego_pipas")
    else:
        form = ReporteRiegoPipasForm(instance=reporte)

    return render(request, "formularios/riego_pipa.html", {"form": form, "numero_reporte":pk})


@login_required
@requiere_grupo("Soldadura")
@es_capturista
def formato_soldadura_editar(request, pk):
    reporte = get_object_or_404(ReporteSoldadura, id=pk)

    if request.method == 'POST':
        form = ReporteSoldaduraForm(request.POST, instance=reporte)
        if form.is_valid():
            form.save()
            return redirect("lista_soldadura")
        else:
            print(form.errors)
    else:
        form = ReporteSoldaduraForm(instance=reporte)

    return render(request, "formularios/soldadura.html", {"form": form, "numero_reporte":pk})

# Convertir booleanos
def draw_checkbox(page, x, y, checked=False):
    if checked:
        page.insert_text((x, y), "X", fontsize=15, color=(0, 0, 0))



# ===================== Generar PDF =====================
@es_capturista
def generar_pdf_cuadrilla(request, pk):
    reporte = ReporteCuadrilla.objects.get(id=pk)
    doc = fitz.open("apps/formularios/plantillas/cuadrilla.pdf")
    page = doc[0]

    # Primera fila
    page.insert_text((150, 100), reporte.distrito, fontsize=8, color=(0,0,1))
    page.insert_text((238, 100), reporte.dia, fontsize=8, color=(0,0,1))
    page.insert_text((470, 100), reporte.fecha.strftime('%d'), fontsize=8, color=(0,0,1))
    page.insert_text((505, 100), reporte.fecha.strftime('%m'), fontsize=8, color=(0,0,1))
    page.insert_text((540, 100), reporte.fecha.strftime('%Y'), fontsize=8, color=(0,0,1))

    # Segunda fila
    draw_checkbox(page, 170, 122, reporte.trabajo_diario)
    draw_checkbox(page, 365, 122, reporte.trabajo_ciudadania)
    draw_checkbox(page, 538, 122, reporte.operativo_especial)

    #Tercera fila - izquierda
    page.insert_text((92, 141), reporte.coordinador, fontsize=8, color=(0,0,1))

    #Cuarta fila
    page.insert_text((138, 155), reporte.encargado_cuadrilla, fontsize=8, color=(0,0,1))
    page.insert_text((420, 160), "# " + str( reporte.folio_pac or ""), fontsize=15, color=(0,0,1))

    #Quinta fila - izquierda
    draw_checkbox(page, 264, 196, reporte.parques_comunitarios)
    draw_checkbox(page, 264, 196, reporte.parques_comunitarios)
    draw_checkbox(page, 264, 210, reporte.parques_municipales)
    draw_checkbox(page, 264, 223, reporte.monumentos_atendidos)
    draw_checkbox(page, 264, 237, reporte.camellones_atendidos)
    draw_checkbox(page, 264, 249, reporte.apoyo_areas_gob)
    draw_checkbox(page, 264, 262, reporte.otros_cant)

    # Quinta fila - derecha
    rect = fitz.Rect(348, 187, 560, 380)
    page.insert_textbox(rect, reporte.trabajo_realizado, fontsize=9, color=(0,0,0), align=0)

    # Sexta fila - izquierda
    page.insert_text((244, 299), str(reporte.superficie_atendida_m2), fontsize=8, color=(0,0,1))
    page.insert_text((244, 312), str(reporte.cesped_cortado_m2), fontsize=8, color=(0,0,1))
    page.insert_text((244, 325), str(reporte.deshierbe_m2), fontsize=8, color=(0,0,1))
    page.insert_text((244, 338), str(reporte.arboles_plantados), fontsize=8, color=(0,0,1))
    page.insert_text((244, 352), str(reporte.arboles_podados), fontsize=8, color=(0,0,1))
    page.insert_text((244, 365), str(reporte.arboles_retirados), fontsize=8, color=(0,0,1))
    page.insert_text((244, 379), str(reporte.zacate_basura_kilos), fontsize=8, color=(0,0,1))
    page.insert_text((244, 393), str(reporte.escombro_kilos), fontsize=8, color=(0,0,1))
    page.insert_text((244, 406), str(reporte.llantas_recolectadas), fontsize=8, color=(0,0,1))
    page.insert_text((244, 419), str(reporte.papeleo_m2), fontsize=8, color=(0,0,1))
    page.insert_text((244, 432), str(reporte.personal_trabajo), fontsize=8, color=(0,0,1))

    # Sexta fila - derecha
    page.insert_text((345, 379), reporte.pendientes, fontsize=8, color=(0,0,1))

    #Séptima fila
    page.insert_text((40, 494), reporte.colonia_camellon, fontsize=8, color=(0,0,1))
    page.insert_text((180, 494), reporte.calle, fontsize=8, color=(0,0,1))
    page.insert_text((406, 494), reporte.ubicacion_area, fontsize=8, color=(0,0,1))

    #Octava fila
    page.insert_text((148, 518), reporte.equipo_utilizado, fontsize=8, color=(0,0,1))
    page.insert_text((148, 532), reporte.material_utilizado, fontsize=8, color=(0,0,1))
    page.insert_text((148, 544), reporte.vehiculos_utilizados, fontsize=8, color=(0,0,1))


    # Guardar en memoria
    buffer = BytesIO()
    doc.save(buffer)
    pdf_bytes = buffer.getvalue()
    doc.close()

    response = HttpResponse(pdf_bytes, content_type="application/pdf")
    fecha_str = reporte.fecha.strftime("%d-%m-%Y")  # Formato día-mes-año
    response["Content-Disposition"] = f'inline; filename="REPORTE_CUADRILLA_#{reporte.folio_pac}_{fecha_str}.pdf"'
    return response

@es_capturista
def generar_pdf_chamizal(request, pk):
    reporte = ReporteChamizal.objects.get(id=pk)
    doc = fitz.open("apps/formularios/plantillas/chamizal.pdf")
    page = doc[0]

    # Primera fila
    page.insert_text((150, 136), reporte.distrito, fontsize=8, color=(0,0,1))
    page.insert_text((435, 135), reporte.dia, fontsize=8, color=(0,0,1))

    page.insert_text((438, 123), reporte.fecha.strftime('%d'), fontsize=8, color=(0,0,1))
    page.insert_text((478, 123), reporte.fecha.strftime('%m'), fontsize=8, color=(0,0,1))
    page.insert_text((518, 123), reporte.fecha.strftime('%Y'), fontsize=8, color=(0,0,1))

    # Segunda fila
    draw_checkbox(page, 170, 155, reporte.trabajo_diario)
    draw_checkbox(page, 330, 155, reporte.trabajo_ciudadania)
    draw_checkbox(page, 508, 155, reporte.operativo_especial)

    #Tercera fila - izquierda
    page.insert_text((110, 175), reporte.coordinador, fontsize=8, color=(0,0,1))

    #Cuarta fila
    page.insert_text((158, 189), reporte.encargado_cuadrilla, fontsize=8, color=(0,0,1))
    page.insert_text((440, 197), "# " + str( reporte.folio_pac or ""), fontsize=15, color=(0,0,1))

    #Quinta fila - izquierda
    draw_checkbox(page, 315, 235, reporte.parque_chamizal)
    draw_checkbox(page, 315, 249, reporte.hoyos)
    draw_checkbox(page, 315, 264, reporte.camellones)
    page.insert_text((90, 275), reporte.otros, fontsize=8,color=(0,0,1))
    draw_checkbox(page, 315, 278, reporte.otros_bool)
    if reporte.otros_bool:
        page.insert_text((290, 237), reporte.otros , fontsize=8,color=(0,0,1))

    # Quinta fila - derecha
    rect_tr = fitz.Rect(373, 224, 565, 280)
    page.insert_textbox(rect_tr, reporte.trabajo_realizado, fontsize=9, color=(0,0,0))

    rect_p = fitz.Rect(373, 397, 565, 430)
    page.insert_textbox(rect_p, reporte.pendientes, fontsize=9, color=(0,0,0))

    rect_o = fitz.Rect(373, 468, 565, 520)
    page.insert_textbox(rect_o, reporte.observaciones, fontsize=9, color=(0,0,0))


    page.insert_text((300, 335), str(reporte.superficie_atendida_m2), fontsize=9, color=(0,0,0))
    page.insert_text((300, 363), str(reporte.cesped_cortado_m2), fontsize=9, color=(0,0,0))
    page.insert_text((300, 392), str(reporte.deshierbe_m2), fontsize=9, color=(0,0,0))
    page.insert_text((300, 420), str(reporte.arboles_plantados), fontsize=9, color=(0,0,0))
    page.insert_text((300, 448), str(reporte.arboles_podados), fontsize=9, color=(0,0,0))
    page.insert_text((300, 476), str(reporte.arboles_retirados), fontsize=9, color=(0,0,0))
    page.insert_text((300, 504), str(reporte.zacate_basura_kilos), fontsize=9, color=(0,0,0))
    page.insert_text((300, 532), str(reporte.papeleo_m2), fontsize=9, color=(0,0,0))
    page.insert_text((300, 560), str(reporte.personal_trabajo), fontsize=9, color=(0,0,0))


    page.insert_text((57, 600), reporte.ubicacion_area, fontsize=9, color=(0,0,0))

    page.insert_text((148, 635), reporte.equipo_utilizado, fontsize=9, color=(0,0,0))
    page.insert_text((148, 662), reporte.material_utilizado, fontsize=9, color=(0,0,0))
    page.insert_text((148, 675), reporte.vehiculos_utilizados, fontsize=9, color=(0,0,0))

    buffer = BytesIO()
    doc.save(buffer)
    pdf_bytes = buffer.getvalue()
    doc.close()

    response = HttpResponse(pdf_bytes, content_type="application/pdf")
    fecha_str = reporte.fecha.strftime("%d-%m-%Y")  # Formato día-mes-año
    response["Content-Disposition"] = f'inline; filename="REPORTE_CHAMIZAL_#{reporte.folio_pac}_{fecha_str}.pdf"'
    return response

@es_capturista
def generar_pdf_cultura(request, pk):
    reporte = ReporteCultura.objects.get(id=pk)
    doc = fitz.open("apps/formularios/plantillas/cultura.pdf")
    page = doc[0]

    #Fechas
    page.insert_text((438, 165), reporte.fecha.strftime('%d'), fontsize=8, color=(0,0,1))
    page.insert_text((465, 165), reporte.fecha.strftime('%m'), fontsize=8, color=(0,0,1))
    page.insert_text((490, 165), reporte.fecha.strftime('%Y'), fontsize=8, color=(0,0,1))

    # Encargado
    page.insert_text((150, 175), reporte.encargado, fontsize=8, color=(0,0,1))

    # Día
    page.insert_text((435, 185), reporte.dia, fontsize=8, color=(0,0,1))

    # Número de Reporte
    page.insert_text((433, 225), "# " + str( reporte.folio_pac or ""), fontsize=15, color=(0,0,1))

    # Lugar
    page.insert_text((125, 247), reporte.lugar, fontsize=8, color=(0,0,1))

    # Personas Beneficiadas
    page.insert_text((220, 278), str(reporte.personas_beneficiadas), fontsize=8, color=(0,0,1))

    # Escuela Atendida
    page.insert_text((220, 295), reporte.escuela_atendida, fontsize=8, color=(0,0,1))

    # Maquiladora Atendida
    page.insert_text((220, 314), reporte.maquiladora_atendida, fontsize=8, color=(0,0,1))

    # Platica Sustentabilidad
    page.insert_text((465, 278), reporte.platica_sustentabilidad, fontsize=8, color=(0,0,1))

    # Curso de Poda
    page.insert_text((465, 295), reporte.curso_poda, fontsize=8, color=(0,0,1))

    # Comité / Parque Atendido
    page.insert_text((465, 314), reporte.comite_parque, fontsize=8, color=(0,0,1))

    # Colonia
    page.insert_text((123, 370), reporte.colonia, fontsize=8, color=(0,0,1))

    # Calle 1
    page.insert_text((164, 406), reporte.calle1, fontsize=8, color=(0,0,1))

    # Calle 2
    page.insert_text((143, 504), reporte.calle2, fontsize=8, rotate=90, color=(0,0,1))

    # Calle 3
    page.insert_text((475, 420), reporte.calle3, fontsize=8, rotate=-90, color=(0,0,1))

    # Calle 4
    page.insert_text((164, 516), reporte.calle4, fontsize=8, color=(0,0,1))

    # Observaciones
    # x = fitz.Rect(x0, y0, x1, y1) 
    rec_o = fitz.Rect(120, 548, 530, 1000)
    page.insert_textbox(rec_o, reporte.observaciones, fontsize=8, color=(0,0,1), lineheight=2)

    # Responsable
    page.insert_text((150, 705), reporte.responsable, fontsize=8, color=(0,0,1))

    # Nombre Ciudadano
    page.insert_text((400, 705), reporte.nombre_ciudadano, fontsize=8, color=(0,0,1))

    buffer = BytesIO()
    doc.save(buffer)
    pdf_bytes = buffer.getvalue()
    doc.close()

    response = HttpResponse(pdf_bytes, content_type="application/pdf")
    fecha_str = reporte.fecha.strftime("%d-%m-%Y")  # Formato día-mes-año
    response["Content-Disposition"] = f'inline; filename="REPORTE_CULTURA_#{reporte.folio_pac}_{fecha_str}.pdf"'
    return response

@es_capturista
def generar_pdf_fuentes(request, pk):
    reporte = ReporteFuentes.objects.get(id=pk)
    doc = fitz.open("apps/formularios/plantillas/fuentes_individual.pdf")
    page = doc[0]

    # Fechas
    page.insert_text((425, 85), reporte.fecha.strftime('%d'), fontsize=8, color=(0,0,1))
    page.insert_text((460, 85), reporte.fecha.strftime('%m'), fontsize=8, color=(0,0,1))
    page.insert_text((496, 85), reporte.fecha.strftime('%Y'), fontsize=8, color=(0,0,1))

    # Encargado
    page.insert_text((145, 99), reporte.encargado, fontsize=8, color=(0,0,1))

    # Día
    page.insert_text((405, 98), reporte.dia, fontsize=8, color=(0,0,1))

    # Número de Reporte
    page.insert_text((428, 137), "# " + str( reporte.folio_pac or ""), fontsize=15, color=(0,0,1))

    # Superficie Atendida
    page.insert_text((215, 150), str(reporte.superficie_atendida_m2), fontsize=8, color=(0,0,1))

    # Limpieza y/o papeleo
    page.insert_text((215, 165), str(reporte.limpieza_papeleo_m2), fontsize=8, color=(0,0,1))

    # Reparacion de Tuberias
    page.insert_text((215, 180), str(reporte.reparacion_tuberia), fontsize=8, color=(0,0,1))

    # Basura Recolectada
    page.insert_text((215, 195), str(reporte.basura_kg), fontsize=8, color=(0,0,1))

    # Reparacion de Bomba
    page.insert_text((490, 150), str(reporte.reparacion_bomba), fontsize=8, color=(0,0,1))

    # Instalación de Bomba
    page.insert_text((490, 165), str(reporte.instalacion_bomba), fontsize=8, color=(0,0,1))

    # Personal que Trabajó
    page.insert_text((490, 180), str(reporte.personal_trabajo), fontsize=8, color=(0,0,1))

    # Colonia
    page.insert_text((50, 235), reporte.colonia, fontsize=8, color=(0,0,1))

    # Calle 1
    page.insert_text((195, 235), reporte.calle1, fontsize=8, color=(0,0,1))

    # Calle 2
    page.insert_text((365, 235), reporte.calle2, fontsize=8, color=(0,0,1))

    # Observaciones
    page.insert_text((50, 260), reporte.observaciones, fontsize=8, color=(0,0,1))

    buffer = BytesIO()
    doc.save(buffer)
    pdf_bytes = buffer.getvalue()
    doc.close()

    response = HttpResponse(pdf_bytes, content_type="application/pdf")
    fecha_str = reporte.fecha.strftime("%d-%m-%Y")  # Formato día-mes-año
    response["Content-Disposition"] = f'inline; filename="REPORTE_FUENTES_#{reporte.folio_pac}_{fecha_str}.pdf"'
    return response

@es_capturista
def generar_pdf_fuentes_multiple(request, ids):
    ids = ids.split(",")
    reportes = ReporteFuentes.objects.filter(id__in=ids)[:4]

    # Plantilla con 4 cuadros en vertical
    doc = fitz.open("apps/formularios/plantillas/fuentes.pdf")
    page = doc[0]

    # Coordenadas de los 4 bloques (verticales)
    bloques = [
        {   # Bloque 1 (arriba)
            "id": (428, 137),
            "superficie": (215, 150), "limpieza": (215, 165), "tuberia": (215, 180),
            "basura": (215, 195), "reparacion_bomba": (490, 150), "instalacion_bomba": (490, 165),
            "personal": (490, 180), "colonia": (50, 235), "calle1": (195, 235), "calle2": (365, 235),
            "observaciones": (50, 260),
        },
        {   # Bloque 2 (segundo rectángulo)
            "dia": (405, 233), "id": (428, 303),
            "superficie": (215, 315), "limpieza": (215, 330), "tuberia": (215, 345),
            "basura": (215, 360), "reparacion_bomba": (490, 315), "instalacion_bomba": (490, 330),
            "personal": (490, 345), "colonia": (50, 403), "calle1": (195, 403), "calle2": (365, 403),
            "observaciones": (50, 433),
        },
        {   # Bloque 3 (tercer rectángulo) – bajado un poco más
            "dia": (405, 403 + 166 + 3),  
            "id": (428, 303 + 166 + 3), 
            "superficie": (215, 315 + 166 + 3), 
            "limpieza": (215, 330 + 166 + 3),
            "tuberia": (215, 345 + 166 + 3),   
            "basura": (215, 360 + 166 + 3),     
            "reparacion_bomba": (490, 315 + 166 + 3), 
            "instalacion_bomba": (490, 330 + 166 + 3), 
            "personal": (490, 345 + 166 + 3),   
            "colonia": (50, 403 + 166 + 3),     
            "calle1": (195, 403 + 166 + 3),    
            "calle2": (365, 403 + 166 + 3),  
            "observaciones": (50, 433 + 166 + 3), 
        },
        {   # Bloque 4 (abajo) – bajado un poco más
            "dia": (405, 403 + 2*166 + 3),
            "id": (428, 303 + 2*166 + 3),   
            "superficie": (215, 315 + 2*166 + 3), 
            "limpieza": (215, 330 + 2*166 + 3),   
            "tuberia": (215, 345 + 2*166 + 3),
            "basura": (215, 360 + 2*166 + 3),    
            "reparacion_bomba": (490, 315 + 2*166 + 3),
            "instalacion_bomba": (490, 330 + 2*166 + 3), 
            "personal": (490, 345 + 2*166 + 3),  
            "colonia": (50, 403 + 2*166 + 3),   
            "calle1": (195, 403 + 2*166 + 3),    
            "calle2": (365, 403 + 2*166 + 3),    
            "observaciones": (50, 433 + 2*166 + 3), 
        },
    ]

    # Insertar datos en cada bloque
    for i, reporte in enumerate(reportes):
        pos = bloques[i]

        page.insert_text(pos["id"], "# " + str(reporte.folio_pac or ""), fontsize=15, color=(0,0,1))

        page.insert_text(pos["superficie"], str(reporte.superficie_atendida_m2 or ""), fontsize=8, color=(0,0,1))
        page.insert_text(pos["limpieza"], str(reporte.limpieza_papeleo_m2 or ""), fontsize=8, color=(0,0,1))
        page.insert_text(pos["tuberia"], str(reporte.reparacion_tuberia or ""), fontsize=8, color=(0,0,1))
        page.insert_text(pos["basura"], str(reporte.basura_kg or ""), fontsize=8, color=(0,0,1))

        page.insert_text(pos["reparacion_bomba"], str(reporte.reparacion_bomba or ""), fontsize=8, color=(0,0,1))
        page.insert_text(pos["instalacion_bomba"], str(reporte.instalacion_bomba or ""), fontsize=8, color=(0,0,1))
        page.insert_text(pos["personal"], str(reporte.personal_trabajo or ""), fontsize=8, color=(0,0,1))

        page.insert_text(pos["colonia"], reporte.colonia or "", fontsize=8, color=(0,0,1))
        page.insert_text(pos["calle1"], reporte.calle1 or "", fontsize=8, color=(0,0,1))
        page.insert_text(pos["calle2"], reporte.calle2 or "", fontsize=8, color=(0,0,1))
        page.insert_text(pos["observaciones"], reporte.observaciones or "", fontsize=8, color=(0,0,1))

    buffer = BytesIO()
    doc.save(buffer)
    pdf_bytes = buffer.getvalue()
    doc.close()

    response = HttpResponse(pdf_bytes, content_type="application/pdf")
    response["Content-Disposition"] = 'inline; filename="REPORTE_FUENTES_MULTIPLE.pdf"'
    return response

@es_capturista
def generar_pdf_fugas(request, pk):
    reporte = ReporteFugas.objects.get(id=pk)
    doc = fitz.open("apps/formularios/plantillas/fugas.pdf")
    page = doc[0]


    page.insert_text((150, 140), reporte.distrito, fontsize=8, color=(0,0,1))
    page.insert_text((435, 140), reporte.dia, fontsize=8, color=(0,0,1))

    page.insert_text((435, 127), reporte.fecha.strftime('%d'), fontsize=8, color=(0,0,1))
    page.insert_text((478, 127), reporte.fecha.strftime('%m'), fontsize=8, color=(0,0,1))
    page.insert_text((518, 127), reporte.fecha.strftime('%Y'), fontsize=8, color=(0,0,1))

    draw_checkbox(page, 150, 160, reporte.trabajo_diario)
    draw_checkbox(page, 320, 160, reporte.trabajo_ciudadania)
    draw_checkbox(page, 508, 160, reporte.operativo_especial)

    page.insert_text((115, 180), reporte.coordinador, fontsize=8, color=(0,0,1))
    page.insert_text((165, 195), reporte.encargado_cuadrilla, fontsize=8, color=(0,0,1))
    page.insert_text((440, 197), "# " + str(reporte.folio_pac or ""), fontsize=15, color=(0,0,1))

    draw_checkbox(page, 300, 245, reporte.parques_comunitarios)
    draw_checkbox(page, 300, 260, reporte.parques_municipales)
    draw_checkbox(page, 300, 275, reporte.monumentos_atendidos)
    draw_checkbox(page, 300, 290, reporte.camellones_atendidos)
    draw_checkbox(page, 300, 305, reporte.apoyo_areas_gob)
    draw_checkbox(page, 300, 320, reporte.otros_cant)

    page.insert_text((85, 319), reporte.otros, fontsize=8, color=(0,0,1))

    page.insert_text((285, 380), str(reporte.superficie_atendida_m2), fontsize=8, color=(0,0,1))
    page.insert_text((285, 410), str(reporte.reparacion_fugas), fontsize=8, color=(0,0,1))
    page.insert_text((285, 440), str(reporte.instalacion_agua), fontsize=8, color=(0,0,1))
    page.insert_text((285, 470), str(reporte.instalacion_riego), fontsize=8, color=(0,0,1))
    page.insert_text((285, 500), str(reporte.revision_riego), fontsize=8, color=(0,0,1))
    page.insert_text((285, 530), str(reporte.material_riego), fontsize=8, color=(0,0,1))
    page.insert_text((285, 560), str(reporte.personal_trabajo), fontsize=8, color=(0,0,1)) #Reemplazar modelo
    page.insert_text((285, 593), str(reporte.personal_trabajo), fontsize=8, color=(0,0,1))

    page.insert_text((57, 660), reporte.colonia, fontsize=8, color=(0,0,1))
    page.insert_text((183, 660), reporte.calle1, fontsize=8, color=(0,0,1))
    page.insert_text((356, 660), reporte.calle2, fontsize=8, color=(0,0,1))

    page.insert_text((135, 690), reporte.equipo_utilizado, fontsize=8, color=(0,0,1))
    page.insert_text((135, 705), reporte.material_utilizado, fontsize=8, color=(0,0,1))
    page.insert_text((148, 733), reporte.vehiculos_utilizados, fontsize=8, color=(0,0,1))
    
    rect_t = fitz.Rect(355, 233, 560, 380)
    page.insert_textbox(rect_t, reporte.trabajo_realizado, fontsize=9, color=(0,0,0))

    rect_p = fitz.Rect(355, 447, 560, 520)
    page.insert_textbox(rect_p, reporte.pendientes, fontsize=9, color=(0,0,0))

    rect_o = fitz.Rect(355, 520, 560, 620)
    page.insert_textbox(rect_o, reporte.observaciones, fontsize=9, color=(0,0,0))

    buffer = BytesIO()
    doc.save(buffer)
    pdf_bytes = buffer.getvalue()
    doc.close()

    response = HttpResponse(pdf_bytes, content_type="application/pdf")
    response["Content-Disposition"] = 'inline; filename="REPORTE_FUGAS_CUADRICULA_DETALLE.pdf"'
    return response

@es_capturista
def generar_pdf_pinturas(request, pk):
    reporte = ReportePintura.objects.get(id=pk)
    doc = fitz.open("apps/formularios/plantillas/pinturas.pdf")
    page = doc[0]

    page.insert_text((128, 135), reporte.distrito, fontsize=8, color=(0,0,1))
    page.insert_text((230, 135), reporte.dia, fontsize=8, color=(0,0,1))

    page.insert_text((435, 135), reporte.fecha.strftime('%d'), fontsize=8, color=(0,0,1))
    page.insert_text((478, 135), reporte.fecha.strftime('%m'), fontsize=8, color=(0,0,1))
    page.insert_text((518, 135), reporte.fecha.strftime('%Y'), fontsize=8, color=(0,0,1))

    draw_checkbox(page, 150, 155, reporte.trabajo_diario)
    draw_checkbox(page, 320, 155, reporte.trabajo_ciudadania)
    draw_checkbox(page, 508, 155, reporte.operativo_especial)

    page.insert_text((115, 175), reporte.coordinador, fontsize=8, color=(0,0,1))
    page.insert_text((165, 190), reporte.encargado, fontsize=8, color=(0,0,1))
    page.insert_text((440, 197), "# " + str(reporte.folio_pac or ""), fontsize=15, color=(0,0,1))

    draw_checkbox(page, 300, 240, reporte.comunitarios_atendidos)
    draw_checkbox(page, 300, 255, reporte.municipales_atendidos)
    draw_checkbox(page, 300, 270, reporte.monumentos_atendidos)
    draw_checkbox(page, 300, 285, reporte.camellones_atendidos)
    draw_checkbox(page, 300, 300, reporte.apoyo_areas_gob)
    draw_checkbox(page, 300, 315, reporte.otros_cant)

    page.insert_text((85, 310), reporte.otros, fontsize=8, color=(0,0,1))

    page.insert_text((285, 360), str(reporte.superficie_atendida_m2), fontsize=8, color=(0,0,1))
    page.insert_text((285, 375), str(reporte.bancas_cemento), fontsize=8, color=(0,0,1))
    page.insert_text((285, 390), str(reporte.bancas_metalicas), fontsize=8, color=(0,0,1))
    page.insert_text((285, 405), str(reporte.multijuegos), fontsize=8, color=(0,0,1))
    page.insert_text((285, 420), str(reporte.resvaladeros), fontsize=8, color=(0,0,1))
    page.insert_text((285, 435), str(reporte.sube_baja), fontsize=8, color=(0,0,1))
    page.insert_text((285, 452), str(reporte.columpios), fontsize=8, color=(0,0,1)) 
    page.insert_text((285, 467), str(reporte.pasamanos), fontsize=8, color=(0,0,1))
    page.insert_text((285, 482), str(reporte.juego_esferas), fontsize=8, color=(0,0,1))
    page.insert_text((285, 497), str(reporte.canchas), fontsize=8, color=(0,0,1))
    page.insert_text((285, 512), str(reporte.porterias), fontsize=8, color=(0,0,1))
    page.insert_text((285, 527), str(reporte.encalado_arboles), fontsize=8, color=(0,0,1))
    page.insert_text((285, 542), str(reporte.levantado_malla), fontsize=8, color=(0,0,1))
    page.insert_text((285, 557), str(reporte.reposicion_malla), fontsize=8, color=(0,0,1))
    page.insert_text((285, 572), str(reporte.pintura_utilizada_litros), fontsize=8, color=(0,0,1))
    page.insert_text((285, 587), str(reporte.thinner_utilizado_litros), fontsize=8, color=(0,0,1))
    page.insert_text((285, 602), str(reporte.personal_trabajo), fontsize=8, color=(0,0,1))


    page.insert_text((57, 667), reporte.colonia, fontsize=8, color=(0,0,1))
    page.insert_text((183, 667), reporte.calle1, fontsize=8, color=(0,0,1))
    page.insert_text((356, 667), reporte.calle2, fontsize=8, color=(0,0,1))

    page.insert_text((185, 703), reporte.equipo_utilizado, fontsize=8, color=(0,0,1))
    page.insert_text((185, 718), reporte.material_utilizado, fontsize=8, color=(0,0,1))
    page.insert_text((185, 733), reporte.vehiculos_utilizados, fontsize=8, color=(0,0,1))
    
    rect_t = fitz.Rect(355, 228, 560, 380)
    page.insert_textbox(rect_t, reporte.trabajo_realizado, fontsize=9, color=(0,0,0), lineheight=1.6)

    rect_p = fitz.Rect(355, 442, 560, 520)
    page.insert_textbox(rect_p, reporte.pendientes, fontsize=9, color=(0,0,0))

    rect_o = fitz.Rect(355, 515, 560, 620)
    page.insert_textbox(rect_o, reporte.observaciones, fontsize=9, color=(0,0,0), lineheight=1.6)

    buffer = BytesIO()
    doc.save(buffer)
    pdf_bytes = buffer.getvalue()
    doc.close()

    response = HttpResponse(pdf_bytes, content_type="application/pdf")
    response["Content-Disposition"] = 'inline; filename="REPORTE_PINTURAS_CUADRICULA_DETALLE.pdf"'
    return response

@es_capturista
def generar_pdf_riego_chamizal(request, pk):
    reporte = ReporteRiegoChamizal.objects.get(id=pk)
    doc = fitz.open("apps/formularios/plantillas/riego_chamizal_individual.pdf")
    page = doc[0]

    # Riengo en
    page.insert_text((280, 73), reporte.riego_en, fontsize=8, color=(0,0,1))

    # Encargado
    page.insert_text((145, 110), reporte.encargado, fontsize=8, color=(0,0,1))

    # Dia
    page.insert_text((400, 110), reporte.dia, fontsize=8, color=(0,0,1))

    # Fecha
    page.insert_text((425, 96), reporte.fecha.strftime('%d'), fontsize=8, color=(0,0,1))
    page.insert_text((460, 96), reporte.fecha.strftime('%m'), fontsize=8, color=(0,0,1))
    page.insert_text((495, 96), reporte.fecha.strftime('%Y'), fontsize=8, color=(0,0,1))

    # Número de Reporte
    page.insert_text((428, 148), "# " + str( reporte.folio_pac or ""), fontsize=15, color=(0,0,1))

    # Superficie Atendida
    page.insert_text((215, 162), str(reporte.superficie_atendida_m2), fontsize=8, color=(0,0,1))

    # Reparación de fugas
    page.insert_text((215, 177), str(reporte.reparacion_fugas), fontsize=8, color=(0,0,1))

    # Limpieza de Aspersores
    page.insert_text((215, 191), str(reporte.limpieza_aspersores), fontsize=8, color=(0,0,1))

    # Basura Recolectada
    page.insert_text((467, 161), str(reporte.basura_recolectada), fontsize=8, color=(0,0,1))

    # Papeleo
    page.insert_text((467, 174), str(reporte.papel_m2), fontsize=8, color=(0,0,1))

    # Personal que Trabajó
    page.insert_text((467, 189), str(reporte.personal_trabajo), fontsize=8, color=(0,0,1))

    # Ubicación
    page.insert_text((50, 222), reporte.ubicacion_area, fontsize=8, color=(0,0,1))

    # Observaciones
    rect_o = fitz.Rect(50, 240, 550, 350)
    page.insert_textbox(rect_o, reporte.observaciones, fontsize=8, lineheight=1.8, color=(0,0,1))

    buffer = BytesIO()
    doc.save(buffer)
    pdf_bytes = buffer.getvalue()
    doc.close()

    response = HttpResponse(pdf_bytes, content_type="application/pdf")
    response["Content-Disposition"] = 'inline; filename="REPORTE_RIEGO_CHAMIZAL.pdf"'
    return response

@es_capturista
def generar_pdf_fuentes_multiple_riego_chamizal(request, ids):
    ids = ids.split(",")
    reportes = ReporteRiegoChamizal.objects.filter(id__in=ids)[:4]

    # Plantilla con 4 cuadros en vertical
    doc = fitz.open("apps/formularios/plantillas/riego_chamizal.pdf")
    page = doc[0]

    # Coordenadas de los 4 bloques (similar a la primera función pero multiplicados hacia abajo)
    bloques = [
        {
            "riego_en": (280, 73), "encargado": (145, 110), "dia": (400, 110),
            "id": (428, 148), "superficie": (215, 162), "fugas": (215, 177),
            "aspersores": (215, 191), "basura": (467, 161), "papel": (467, 174),
            "personal": (467, 189), "ubicacion": (50, 222), "observaciones": fitz.Rect(50, 240, 550, 350)
        },
        {
            "id": (428, 148 + 156), "superficie": (215, 162 + 156), "fugas": (215, 177 + 156),
            "aspersores": (215, 191 + 156), "basura": (467, 161 + 156), "papel": (467, 174 + 156),
            "personal": (467, 189 + 156), "ubicacion": (50, 222 + 170), "observaciones": fitz.Rect(50, 240 + 170, 550, 350 + 200)
        },
        {
            "id": (428, 148 + 327), "superficie": (215, 162 + 327), "fugas": (215, 177 + 327),
            "aspersores": (215, 191 + 327), "basura": (467, 161 + 327), "papel": (467, 174 + 327),
            "personal": (467, 189 + 327), "ubicacion": (50, 222 + 339), "observaciones": fitz.Rect(50, 240 + 339, 550, 350 + 339)
        },
        {
            "id": (428, 148 + 494), "superficie": (215, 162 + 494), "fugas": (215, 177 + 494),
            "aspersores": (215, 191 + 494), "basura": (467, 161 + 494), "papel": (467, 174 + 494),
            "personal": (467, 189 + 494), "ubicacion": (50, 222 + 505), "observaciones": fitz.Rect(50, 240 + 505, 550, 350 + 505)
        }
    ]

    # Insertar datos en cada bloque
    for i, reporte in enumerate(reportes):
        pos = bloques[i]

        page.insert_text(pos["id"], "# " + str(reporte.folio_pac or ""), fontsize=15, color=(0,0,1))
        page.insert_text(pos["superficie"], str(reporte.superficie_atendida_m2 or ""), fontsize=8, color=(0,0,1))
        page.insert_text(pos["fugas"], str(reporte.reparacion_fugas or ""), fontsize=8, color=(0,0,1))
        page.insert_text(pos["aspersores"], str(reporte.limpieza_aspersores or ""), fontsize=8, color=(0,0,1))
        page.insert_text(pos["basura"], str(reporte.basura_recolectada or ""), fontsize=8, color=(0,0,1))
        page.insert_text(pos["papel"], str(reporte.papel_m2 or ""), fontsize=8, color=(0,0,1))
        page.insert_text(pos["personal"], str(reporte.personal_trabajo or ""), fontsize=8, color=(0,0,1))
        page.insert_text(pos["ubicacion"], reporte.ubicacion_area or "", fontsize=8, color=(0,0,1))

        # Observaciones (cuadro de texto)
        page.insert_textbox(pos["observaciones"], reporte.observaciones or "", fontsize=8, lineheight=1.8, color=(0,0,1))

    buffer = BytesIO()
    doc.save(buffer)
    pdf_bytes = buffer.getvalue()
    doc.close()

    response = HttpResponse(pdf_bytes, content_type="application/pdf")
    response["Content-Disposition"] = 'inline; filename="REPORTE_RIEGO_CHAMIZAL_MULTIPLE.pdf"'
    return response

@es_capturista
def generar_pdf_riego_pipa(request, pk):
    reporte = ReporteRiegoPipas.objects.get(id=pk)
    doc = fitz.open("apps/formularios/plantillas/riego_pipa_individual.pdf")
    page = doc[0]

    # Fechas
    page.insert_text((435, 125), reporte.fecha.strftime('%d'), fontsize=8, color=(0,0,1))
    page.insert_text((480, 125), reporte.fecha.strftime('%m'), fontsize=8, color=(0,0,1))
    page.insert_text((520, 125), reporte.fecha.strftime('%Y'), fontsize=8, color=(0,0,1))

    # Día
    page.insert_text((415, 140), reporte.dia, fontsize=8, color=(0,0,1))

    # Número de Reporte
    page.insert_text((265, 140), "# " + str( reporte.folio_pac or ""), fontsize=15, color=(0,0,1))

    # Nombre del Chofer
    page.insert_text((200, 155), reporte.nombre_chofer, fontsize=8, color=(0,0,1))

    # Nombre del Ayudante
    page.insert_text((200, 170), reporte.nombre_ayudante, fontsize=8, color=(0,0,1))

    # Engomado del Vehiculo
    page.insert_text((200, 185), reporte.engomado_vehiculo, fontsize=8, color=(0,0,1))

    # Hora de Salida
    page.insert_text((200, 200), reporte.hora_salida.strftime('%H:%M'), fontsize=8, color=(0,0,1))

    # Hora de Regreso
    page.insert_text((200, 215), reporte.hora_regreso.strftime('%H:%M'), fontsize=8, color=(0,0,1))

    # Avenida o Lugar de Riego
    page.insert_text((200, 229), reporte.lugar_riego, fontsize=8, color=(0,0,1))

    # Colonia
    page.insert_text((53, 290), reporte.colonia, fontsize=6, color=(0,0,1))

    # Calle 1
    page.insert_text((195, 290), reporte.calle1, fontsize=6, color=(0,0,1))

    # Calle 2
    page.insert_text((360, 290), reporte.calle2, fontsize=6, color=(0,0,1))

    # Viajes Realizados
    page.insert_text((120, 337), str(reporte.viajes), fontsize=8, color=(0,0,1))

    # Agua Empleada en Litros
    page.insert_text((360, 337), str(reporte.agua_empleada_litros), fontsize=8, color=(0,0,1))

    # Observaciones
    rect_o = fitz.Rect(117, 370, 480, 450)
    page.insert_textbox(rect_o, reporte.observaciones, fontsize=7, lineheight=1.8, color=(0,0,1))


    buffer = BytesIO()
    doc.save(buffer)
    pdf_bytes = buffer.getvalue()
    doc.close()

    response = HttpResponse(pdf_bytes, content_type="application/pdf")
    response["Content-Disposition"] = 'inline; filename="REPORTE_RIEGO_PIPA.pdf"'
    return response

@es_capturista
def generar_pdf_riego_pipa_multiple(request, ids):
    ids = ids.split(",")
    reportes = ReporteRiegoPipas.objects.filter(id__in=ids)[:4]

    # Plantilla con 4 cuadros en vertical
    doc = fitz.open("apps/formularios/plantillas/riego_pipa.pdf")
    page = doc[0]

    # Coordenadas de los 4 bloques (cada 200px hacia abajo)
    bloques = [
        {
            "fecha_d": (435, 125), "fecha_m": (480, 125), "fecha_y": (520, 125),
            "dia": (415, 140), "id": (265, 140),
            "chofer": (200, 155), "ayudante": (200, 170), "engomado": (200, 185),
            "salida": (200, 200), "regreso": (200, 215), "lugar": (200, 229),
            "colonia": (53, 290), "calle1": (195, 290), "calle2": (360, 290),
            "viajes": (120, 337), "agua": (360, 337),
            "observaciones": fitz.Rect(117, 370, 480, 450)
        },
        {
            "fecha_d": (435, 125 + 340), "fecha_m": (480, 125 + 340), "fecha_y": (520, 125 + 340),
            "dia": (415, 140 + 340), "id": (265, 140 + 340),
            "chofer": (200, 155 + 340), "ayudante": (200, 170 + 340), "engomado": (200, 185 + 340),
            "salida": (200, 200 + 340), "regreso": (200, 215 + 340), "lugar": (200, 229 + 340),
            "colonia": (53, 290 + 340), "calle1": (195, 290 + 340), "calle2": (360, 290 + 340),
            "viajes": (120, 337 + 345), "agua": (360, 337 + 345),
            "observaciones": fitz.Rect(117, 370 + 345, 480, 450 + 345)
        }
    ]

    # Insertar datos en cada bloque
    for i, reporte in enumerate(reportes):
        pos = bloques[i]

        # Fecha
        if reporte.fecha:
            page.insert_text(pos["fecha_d"], reporte.fecha.strftime('%d'), fontsize=8, color=(0,0,1))
            page.insert_text(pos["fecha_m"], reporte.fecha.strftime('%m'), fontsize=8, color=(0,0,1))
            page.insert_text(pos["fecha_y"], reporte.fecha.strftime('%Y'), fontsize=8, color=(0,0,1))

        # Día e ID
        page.insert_text(pos["dia"], str(reporte.dia or ""), fontsize=8, color=(0,0,1))
        page.insert_text(pos["id"], "# " + str(reporte.folio_pac or ""), fontsize=15, color=(0,0,1))

        # Datos del chofer y vehículo
        page.insert_text(pos["chofer"], reporte.nombre_chofer or "", fontsize=8, color=(0,0,1))
        page.insert_text(pos["ayudante"], reporte.nombre_ayudante or "", fontsize=8, color=(0,0,1))
        page.insert_text(pos["engomado"], reporte.engomado_vehiculo or "", fontsize=8, color=(0,0,1))

        # Horas
        if reporte.hora_salida:
            page.insert_text(pos["salida"], reporte.hora_salida.strftime('%H:%M'), fontsize=8, color=(0,0,1))
        if reporte.hora_regreso:
            page.insert_text(pos["regreso"], reporte.hora_regreso.strftime('%H:%M'), fontsize=8, color=(0,0,1))

        # Lugar y dirección
        page.insert_text(pos["lugar"], reporte.lugar_riego or "", fontsize=8, color=(0,0,1))
        page.insert_text(pos["colonia"], reporte.colonia or "", fontsize=6, color=(0,0,1))
        page.insert_text(pos["calle1"], reporte.calle1 or "", fontsize=6, color=(0,0,1))
        page.insert_text(pos["calle2"], reporte.calle2 or "", fontsize=6, color=(0,0,1))

        # Datos de riego
        page.insert_text(pos["viajes"], str(reporte.viajes or ""), fontsize=8, color=(0,0,1))
        page.insert_text(pos["agua"], str(reporte.agua_empleada_litros or ""), fontsize=8, color=(0,0,1))

        # Observaciones
        page.insert_textbox(pos["observaciones"], reporte.observaciones or "", fontsize=7, lineheight=1.8, color=(0,0,1))

    buffer = BytesIO()
    doc.save(buffer)
    pdf_bytes = buffer.getvalue()
    doc.close()

    response = HttpResponse(pdf_bytes, content_type="application/pdf")
    response["Content-Disposition"] = 'inline; filename="REPORTE_RIEGO_PIPA_MULTIPLE.pdf"'
    return response

@es_capturista
def generar_pdf_soldadura(request, pk):
    reporte = ReporteSoldadura.objects.get(id=pk)
    doc = fitz.open("apps/formularios/plantillas/soldadura.pdf")
    page = doc[0]

    page.insert_text((128, 135), reporte.distrito, fontsize=8, color=(0,0,1))
    page.insert_text((230, 135), reporte.dia, fontsize=8, color=(0,0,1))

    page.insert_text((435, 135), reporte.fecha.strftime('%d'), fontsize=8, color=(0,0,1))
    page.insert_text((478, 135), reporte.fecha.strftime('%m'), fontsize=8, color=(0,0,1))
    page.insert_text((518, 135), reporte.fecha.strftime('%Y'), fontsize=8, color=(0,0,1))

    draw_checkbox(page, 150, 155, reporte.trabajo_diario)
    draw_checkbox(page, 320, 155, reporte.trabajo_ciudadania)
    draw_checkbox(page, 508, 155, reporte.operativo_especial)

    page.insert_text((115, 175), reporte.coordinador, fontsize=8, color=(0,0,1))
    page.insert_text((165, 190), reporte.encargado, fontsize=8, color=(0,0,1))
    page.insert_text((440, 197), "# " + str(reporte.folio_pac or " "), fontsize=15, color=(0,0,1))

    draw_checkbox(page, 300, 240, reporte.comunitarios_atendidos)
    draw_checkbox(page, 300, 255, reporte.municipales_atendidos)
    draw_checkbox(page, 300, 270, reporte.monumentos_atendidos)
    draw_checkbox(page, 300, 285, reporte.camellones_atendidos)
    draw_checkbox(page, 300, 300, reporte.apoyo_areas_gob)
    draw_checkbox(page, 300, 315, reporte.otros_cant)

    page.insert_text((85, 310), reporte.otros, fontsize=8, color=(0,0,1))

    page.insert_text((285, 360), str(reporte.superficie_atendida_m2), fontsize=8, color=(0,0,1))
    #page.insert_text((285, 375), str(reporte.bancas_cemento), fontsize=8, color=(0,0,1))
    page.insert_text((285, 375), str(reporte.bancas_metalicas), fontsize=8, color=(0,0,1))
    #page.insert_text((285, 405), str(reporte.multijuegos), fontsize=8, color=(0,0,1))
    page.insert_text((285, 390), str(reporte.resbaladeros), fontsize=8, color=(0,0,1))
    page.insert_text((285, 407), str(reporte.sube_baja), fontsize=8, color=(0,0,1))
    page.insert_text((285, 422), str(reporte.columpios), fontsize=8, color=(0,0,1)) 
    page.insert_text((285, 437), str(reporte.pasamanos), fontsize=8, color=(0,0,1))
    page.insert_text((285, 452), str(reporte.juego_esferas), fontsize=8, color=(0,0,1))
    page.insert_text((285, 467), str(reporte.canchas), fontsize=8, color=(0,0,1))
    page.insert_text((285, 482), str(reporte.porterias), fontsize=8, color=(0,0,1))
    #page.insert_text((285, 527), str(reporte.encalado_arboles), fontsize=8, color=(0,0,1))
    page.insert_text((285, 497), str(reporte.levantado_malla), fontsize=8, color=(0,0,1))
    page.insert_text((285, 512), str(reporte.reposicion_malla), fontsize=8, color=(0,0,1))
    #page.insert_text((285, 572), str(reporte.pintura_utilizada_litros), fontsize=8, color=(0,0,1))
    page.insert_text((285, 527), str(reporte.thinner_utilizado_litros), fontsize=8, color=(0,0,1))
    page.insert_text((285, 542), str(reporte.personal_trabajo), fontsize=8, color=(0,0,1))


    page.insert_text((57, 638), reporte.colonia, fontsize=8, color=(0,0,1))
    page.insert_text((187, 638), reporte.calle1, fontsize=8, color=(0,0,1))
    page.insert_text((357, 638), reporte.calle2, fontsize=8, color=(0,0,1))

    page.insert_text((185, 670), reporte.equipo_utilizado, fontsize=8, color=(0,0,1))
    page.insert_text((185, 685), reporte.material_utilizado, fontsize=8, color=(0,0,1))
    page.insert_text((185, 700), reporte.vehiculos_utilizados, fontsize=8, color=(0,0,1))
    
    rect_t = fitz.Rect(358, 228, 560, 380)
    page.insert_textbox(rect_t, reporte.trabajo_realizado, fontsize=9, color=(0,0,0), lineheight=1.6)

    rect_p = fitz.Rect(358, 410, 560, 520)
    page.insert_textbox(rect_p, reporte.pendientes, fontsize=9, color=(0,0,0))

    rect_o = fitz.Rect(358, 485, 560, 620)
    page.insert_textbox(rect_o, reporte.observaciones, fontsize=9, color=(0,0,0), lineheight=1.6)

    buffer = BytesIO()
    doc.save(buffer)
    pdf_bytes = buffer.getvalue()
    doc.close()

    response = HttpResponse(pdf_bytes, content_type="application/pdf")
    response["Content-Disposition"] = 'inline; filename="REPORTE_PINTURAS_CUADRICULA_DETALLE.pdf"'
    return response


# ===================== Funcionamiento offline =======================

FORMULARIOS = {
    'cuadrilla': ReporteCuadrillaForm,
    'chamizal': ReporteChamizalForm,
    'cultura': ReporteCulturaForm,
    'fuentes': ReporteFuentesForm,
    'fugas': ReporteFugasForm,
    'pinturas': ReportePinturasForm,
    'riego_chamizal': ReporteRiegoChamizalForm,
    'riego_pipa': ReporteRiegoPipasForm,
}

@csrf_exempt
@require_POST
def api_guardar_generico(request, form_name):
    try:
        form_class = FORMULARIOS.get(form_name)
        if not form_class:
            return JsonResponse({'status': 'error', 'message': 'Formulario no encontrado'}, status=404)

        data = json.loads(request.body)
        form = form_class(data)
        if form.is_valid():
            instance = form.save()
            return JsonResponse({'status': 'ok', 'id': instance.id}, status=201)
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
