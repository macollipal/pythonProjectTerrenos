from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Corte as Corte, Ubicacion as Ubicacion, Existe, Riesgo, Eval_Terrenos, Comuna, EstadoDiseno,PeriodoCarga


# Register your models here.


class CorteAdmin(admin.ModelAdmin):
    list_display = (
        'id_corte', 'nombre_cor',
        'descripcion_cor')  # define campos de la clase taller a ver en panel de administración
    list_display_links = ['id_corte', 'nombre_cor',
                          'descripcion_cor']  # indica los campos que llevan al menú de modificación
    search_fields = ('nombre_cor',)  # crea un buscador por nombre taller
    list_filter = [
        'nombre_cor']  # crea un filtro de busqueda (Es muy potente con fechas permite filtrar por ventas de la semana o mes
    # date_hierarchy = "fecha" para combinar cuando filtras por fecha


class UbicacionAdmin(admin.ModelAdmin):
    list_display = (
        'id_ubicacion', 'bip_ubi', 'corte_ubi',
        'comuna_ubi', 'latitud_ubi', 'longitud_ubi','unidad_destino_ubi')  # define campos de la clase taller a ver en panel de administración
    list_display_links = ['bip_ubi']


class ExisteAdmin(admin.ModelAdmin):
    list_display = (
        'id_existe', 'nombre_exi', 'valor_exi')  # define campos de la clase taller a ver en panel de administración
    list_display_links = ['nombre_exi']


class RiesgoAdmin(admin.ModelAdmin):
    list_display = (
        'id_riesgo', 'nombre_rie', 'valor_rie')  # define campos de la clase taller a ver en panel de administración
    list_display_links = ['nombre_rie']


class ComunaAdmin(admin.ModelAdmin):
    list_display = (
        'id_comuna', 'nombre_com', 'zona_com')  # define campos de la clase taller a ver en panel de administración
    list_display_links = ['nombre_com']

class EstadoDisenoAdmin(admin.ModelAdmin):
    list_display = (
        'id_estado', 'nombre_est', 'valor_est')  # define campos de la clase taller a ver en panel de administración
    list_display_links = ['nombre_est']

class PeriodoCargaAdmin(admin.ModelAdmin):
    list_display = (
        'id_periodo', 'fecha_per', 'nombre_per')  # define campos de la clase taller a ver en panel de administración
    list_display_links = ['fecha_per','nombre_per']

class Eval_TerrenosAdmin(admin.ModelAdmin):
    list_display = ('fecha_carga_ter',
        'id_eval_terrenos', 'ubicacion_ter', 'existe_guaria_ter', 'existe_gasto_ter', 'riesgo_incendio_ter',
        'riesgo_incendio_ter',
        'riesgo_intrusion_ter')  # define campos de la clase taller a ver en panel de administración
    list_display_links = ['ubicacion_ter']


admin.site.register(Corte, CorteAdmin)
admin.site.register(Ubicacion, UbicacionAdmin)
admin.site.register(Existe, ExisteAdmin)
admin.site.register(Riesgo, RiesgoAdmin)
admin.site.register(Comuna, ComunaAdmin)
admin.site.register(EstadoDiseno, EstadoDisenoAdmin)
admin.site.register(PeriodoCarga, PeriodoCargaAdmin)
admin.site.register(Eval_Terrenos, Eval_TerrenosAdmin)
