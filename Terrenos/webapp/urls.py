
from django.urls import path


from . import views

urlpatterns = {
    path('', views.index, name='index'),
    path('CrudUbicacion', views.CrudUbicacion, name='CrudUbicacion'),
    path('CrudUbicacion/<int:buscarId>/', views.CrudUbicacionRead, name='CrudUbicacion'),
    path('CrudCorte', views.CrudCorte, name='CrudCorte'),
    path('CrudCorte/<int:buscarId>/', views.CrudCorteRead, name='CrudCorte'),
    path('CrudTerreno', views.CrudTerreno, name='CrudTerreno'),
    path('CrudTerreno/<int:buscarId>/', views.CrudTerrenoRead, name='CrudTerreno'),
    path('CrudPeriodoCarga', views.CrudPeriodoCarga, name='CrudPeriodoCarga'),
    path('CrudPeriodoCarga/<int:buscarId>/', views.CrudPeriodoCargaRead, name='CrudPeriodoCarga'),


}


