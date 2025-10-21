from django.urls import path
from . import views

urlpatterns = [
    path('base', views.plantilla, name="plantilla"),
    path('menu/', views.menu_botones, name="menu"),

    #Cuadrillas
    path('cuadrillas/', views.formato_cuadrilla, name="generar_cuadrillas"),
    path('lista/', views.lista_cuadrilla, name='lista_cuadrillas'),
    path('cuadrillas/editar/<int:pk>', views.formato_cuadrilla_editar, name="cuadrilla_editar"),
    path('reporte/pdf/<int:pk>/', views.generar_pdf_cuadrilla, name='reporte_pdf'),

    #Chamizal
    path('chamizal/', views.formato_chamizal, name="generar_chamizal"),
    path('chamizal/lista/', views.lista_chamizal, name='lista_chamizal'),
    path('chamizal/editar/<int:pk>', views.formato_chamizal_editar, name="chamizal_editar"),
    path('chamizal/reporte/pdf/<int:pk>/', views.generar_pdf_chamizal, name='reporte_pdf_chamizal'),

    #Cultura
    path('cultura/', views.formato_cultura, name="generar_cultura"),
    path('cultura/lista/', views.lista_cultura, name='lista_cultura'),
    path('cultura/editar/<int:pk>', views.formato_cultura_editar, name="cultura_editar"),
    path('cultura/reporte/pdf/<int:pk>/', views.generar_pdf_cultura, name='reporte_pdf_cultura'),

    #Fuentes
    path('fuentes/', views.formato_fuentes, name="generar_fuentes"),
    path('fuentes/lista/', views.lista_fuentes, name='lista_fuentes'),
    path('fuentes/editar/<int:pk>', views.formato_fuentes_editar, name="fuentes_editar"),
    path('fuentes/reporte/pdf/<int:pk>/', views.generar_pdf_fuentes, name='reporte_pdf_fuentes'),
    path('fuentes/reporte/pdf-multiple/<str:ids>', views.generar_pdf_fuentes_multiple, name='generar_fuentes'),

    #Fugas
    path('fugas/', views.formato_fugas, name="generar_fugas"),
    path('fugas/lista/', views.lista_fugas, name='lista_fugas'),
    path('fugas/editar/<int:pk>', views.formato_fugas_editar, name="fugas_editar"),
    path('fugas/reporte/pdf/<int:pk>/', views.generar_pdf_fugas, name='reporte_pdf_fugas'),

    #Pinturas
    path('pinturas/', views.formato_pinturas, name="generar_pinturas"),
    path('pinturas/lista/', views.lista_pintura, name='lista_pinturas'),
    path('pinturas/editar/<int:pk>', views.formato_pinturas_editar, name="pinturas_editar"),
    path('pinturas/reporte/pdf/<int:pk>/', views.generar_pdf_pinturas, name='reporte_pdf_pinturas'),

    #Riego Chamizal
    path('riego_chamizal/', views.formato_riego_chamizal, name="generar_riego_chamizal"),
    path('riego_chamizal/lista/', views.lista_riego_chamizal, name='lista_riego_chamizal'),
    path('riego_chamizal/editar/<int:pk>', views.formato_riego_chamizal_editar, name="riego_chamizal_editar"),
    path('riego_chamizal/reporte/pdf/<int:pk>/', views.generar_pdf_riego_chamizal, name='reporte_pdf_riego_chamizal'),
    path('riego_chamizal/reporte/pdf-multiple/<str:ids>', views.generar_pdf_fuentes_multiple_riego_chamizal, name='generar_pdf_riego_chamizal_multiple'),

    #Riego pipas
    path('riego_pipas/', views.formato_riego_pipas, name="generar_riego_pipas"),
    path('riego_pipas/lista/', views.lista_riego_pipas, name='lista_riego_pipas'),
    path('riego_pipas/editar/<int:pk>', views.formato_riego_pipas_editar, name="riego_pipas_editar"),
    path('riego_pipas/reporte/pdf/<int:pk>/', views.generar_pdf_riego_pipa, name='reporte_pdf_riego_pipas'),
    path('riego_pipas/reporte/pdf-multiple/<str:ids>', views.generar_pdf_riego_pipa_multiple, name='generar_pdf_riego_pipas_multiple'),



    #Funcionamiento offline
    path('api/<str:form_name>/', views.api_guardar_generico,),



]