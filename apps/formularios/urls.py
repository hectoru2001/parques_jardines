from django.urls import path
from . import views

urlpatterns = [
    path('base', views.plantilla, name="plantilla"),
    path('menu/', views.menu_botones, name="menu"),

    path('formulario/<str:tipo_reporte>/', views.generar_formato, name='generar_formato'),
    path('lista/<str:tipo_reporte>/', views.lista_reportes, name='lista_reportes'),
    path('reportes/modal/<str:tipo_reporte>/<int:pk>/', views.modal_reporte, name='modal_reporte_edit'),
    path("reportes/folio_pac/<str:tipo>/<int:pk>/", views.editar_folio_pac, name="editar_folio_pac"),
    path("formulario/<str:tipo_reporte>/editar/<int:pk>/", views.editar_reporte, name="editar_reporte"),


    #Cuadrillas
    path('reporte/pdf/<int:pk>/', views.generar_pdf_cuadrilla, name='reporte_pdf'),

    #Chamizal
    path('chamizal/reporte/pdf/<int:pk>/', views.generar_pdf_chamizal, name='reporte_pdf_chamizal'),

    #Cultura
    path('cultura/reporte/pdf/<int:pk>/', views.generar_pdf_cultura, name='reporte_pdf_cultura'),

    #Fuentes
    path('fuentes/reporte/pdf/<int:pk>/', views.generar_pdf_fuentes, name='reporte_pdf_fuentes'),
    path('fuentes/reporte/pdf-multiple/<str:ids>', views.generar_pdf_fuentes_multiple, name='generar_fuentes'),

    #Fugas
    path('fugas/reporte/pdf/<int:pk>/', views.generar_pdf_fugas, name='reporte_pdf_fugas'),

    #Pinturas
    path('pinturas/reporte/pdf/<int:pk>/', views.generar_pdf_pinturas, name='reporte_pdf_pinturas'),

    #Riego Chamizal
    path('riego_chamizal/reporte/pdf/<int:pk>/', views.generar_pdf_riego_chamizal, name='reporte_pdf_riego_chamizal'),
    path('riego_chamizal/reporte/pdf-multiple/<str:ids>', views.generar_pdf_fuentes_multiple_riego_chamizal, name='generar_pdf_riego_chamizal_multiple'),

    #Riego pipas
    path('riego_pipas/reporte/pdf/<int:pk>/', views.generar_pdf_riego_pipa, name='reporte_pdf_riego_pipas'),
    path('riego_pipas/reporte/pdf-multiple/<str:ids>', views.generar_pdf_riego_pipa_multiple, name='generar_pdf_riego_pipas_multiple'),

    #Riego pipas
    path('soldadura/reporte/pdf/<int:pk>/', views.generar_pdf_soldadura, name='reporte_pdf_soldadura'),

    #Funcionamiento offline
    path('api/<str:form_name>/', views.api_guardar_generico,),



]