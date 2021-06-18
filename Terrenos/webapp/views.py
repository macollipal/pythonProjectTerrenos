# Create your views here.

# from django.contrib import auth
# from django.contrib.auth.models import User

# from django.views.generic import TemplateView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection
from crud.models import Corte as CO, Ubicacion as UB, Eval_Terrenos as TE, Existe as EX, Riesgo as RI, \
    EstadoDiseno as ED, Comuna as COM, PeriodoCarga as PER

# para la API-------------------------------
from webapp.serializers import CorteSerializer, ExisteSerializer, UbicacionSerializer
from rest_framework import generics


# para la API-------------------------------

# -------------------------------------------

# las funciones funcionan sobre el crud
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.decorators import permission_required

# Create your views here.

# class CorteView(LoginRequiredMixin, TemplateView):
#    template_name = 'crud_ubicacion.html'

# class CorteViewPermission(PermissionRequiredMixin, TemplateView):
#    template_name = 'crud_ubicacion.html'
#    permission_required = 'crud.view_taller'

# class CorteViewPermissionLP(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
#    template_name = 'crud_ubicacion.html'
#    permission_required = 'crud.view_taller'


def index(request):
    sedes = [{'sede': 'Viña del Mar',
              'direccion': '1 Norte 45'},
             {'sede': 'Santiago',
              'direccion': 'Estado 21'},
             ]
    # carreras = CA.objects.all()
    contexto = {'sedes': sedes, 'carreras': 0}
    return render(request, 'index.html', contexto)


# class CrudTallerView(LoginRequiredMixin, TemplateView):
#    template_name = 'crud_ubicacion.html'


# @login_required
def CrudCorte(request):
    aviso = ''
    corte = ''
    # Detecta si haay una petición

    if request.method == "POST":
        post = request.POST
        id = int('0' + post['txt_id_cor'])
        corte_ = post['txt_nombre_cor']
        descripcion = post['txt_desc_cor']

        item = {}
        listado = {}

        # detecta si el botón guardar fue presionado
        if 'btnGuardar' in post:
            # Si id es menor que  1, es nueva información (INSERT)
            # caso contrario lo modifica
            if id < 1:  # Valida si el usuario tiene permiso para añadir información a la tabla
                try:
                    CO.objects.create(nombre_cor=corte_,
                                      descripcion_cor=descripcion)
                    aviso = 'Registrando datos'
                except:
                    aviso = 'ya se encuentra registrado'

            elif id > 0:
                item = CO.objects.get(id_corte=id)
                item.nombre_cor = corte_
                item.descripcion_cor = descripcion
                item.save()

                aviso = 'Registrando datos'

        elif 'btnEliminar' in post:
            item = CO.objects.get(id_corte=id)
            item.delete()
            aviso = 'Eliminando el registro'
            item = {}

        elif 'btnListar' in post:
            listado = CO.objects.all()

        contexto = {'item': item, 'listado': listado, 'corte': corte, 'aviso': aviso, }
    else:
        contexto = {'corte': corte}
    # renderiza respuesta usando plantilla y contexto

    return render(request, 'crud_corte.html', contexto)


def CrudCorteRead(request, buscarId):
    item = CO.objects.get(pk=buscarId)

    contexto = {'item': item}
    return render(request, 'crud_corte.html', contexto)


def CrudUbicacion(request):
    aviso = ''
    aviso2 = ''
    corte = CO.objects.all()
    comuna = COM.objects.all()
    # Detecta si haay una petición

    if request.method == "POST":
        post = request.POST
        id = int('0' + post['txt_id'])
        bip = post['txt_bip']
        _corte = post['cmbCorte']
        _comuna = post['cmbComuna']
        direccion = post['txt_direccion']
        latitud = post['txt_latitud']
        longitud = post['txt_longitud']
        udestino = post['txt_udestino']

        item = {}
        item2 = {}
        listado = {}
        listado2 = {}

        # detecta si el botón guardar fue presionado
        if 'btnGuardar' in post:
            # Si id es menor que  1, es nueva información (INSERT)
            # caso contrario lo modifica
            if id < 1:  # Valida si el usuario tiene permiso para añadir información a la tabla
                try:
                    UB.objects.create(bip_ubi=bip,
                                      direccion_ubi=direccion,
                                      latitud_ubi=latitud,
                                      longitud_ubi=longitud,
                                      unidad_destino_ubi=udestino,
                                      corte_ubi_id=_corte,
                                      comuna_ubi_id=_comuna)
                    aviso = 'Registrando datos' + str(id)
                except:
                    aviso = 'ya se encuentra registrado' + str(id) + _corte

            elif id > 0:
                item = UB.objects.get(id_ubicacion=id)
                # item.bip_ubi = bip
                item.corte_ubi_id = _corte

                item.comuna_ubi_id = _comuna
                item.direccion_ubi = direccion
                item.latitud_ubi = latitud
                item.longitud_ubi = longitud
                item.unidad_destino_ubi = udestino

                item.save()

                aviso = 'Modificando datos'

        elif 'btnEliminar' in post:
            item = UB.objects.get(id_ubicacion=id)
            item.delete()
            aviso = 'Eliminando el registro'
            item = {}

        elif 'btnListar' in post:
            listado = UB.objects.all()
        
        elif 'btnBuscar' in post:

            #if bip != '':  # Valida si el usuario tiene permiso para añadir información a la tabla
            try:
                item = UB.objects.filter(bip_ubi=1).values()


               
                aviso = 'Busqueda correcta :' + str(id)  + ' - ' +str(bip) + ' - ' + str(_corte) + ' - '

            except:
                    aviso = 'Busqueda Implacable' + ' - ' + str(bip) + ' - ' + str(id) 

        contexto = {'item': item, 'listado': listado, 'aviso': aviso, 'corte': corte, 'comuna': comuna}
       
    else:
        contexto = {'corte': corte, 'comuna': comuna}
    # renderiza respuesta usando plantilla y contexto

    return render(request, 'crud_ubicacion.html', contexto)


def CrudUbicacionRead(request, buscarId):
    item = UB.objects.get(pk=buscarId)
    corte = CO.objects.all()
    comuna = COM.objects.all()
    contexto = {'item': item, 'corte': corte, 'comuna': comuna}
    return render(request, 'crud_ubicacion.html', contexto)


def CrudTerreno(request):
    aviso = ''
    terreno = ''

    existe = EX.objects.all()
    riesgo = RI.objects.all()
    estadodiseno = ED.objects.all()
    ubicacion = UB.objects.all()
    periodo = PER.objects.all()

    # Detecta si haay una petición
    if request.method == "POST":
        post = request.POST
        id = int('0' + post['txt_id_ter'])
        fecha = post['cmb_fechacarga_ter']
        bip = post['cmbBip']
        m2 = post['txt_m2']
        estado = post['cmbEstadoDiseno']
        id_intrusion = post['cmbRiesgoIntrucion']
        id_incendio = post['cmbRiesgoIncendio']
        id_gasto = post['cmbExisteGasto']
        id_guardia = post['cmbExisteGuardia']
        id_constru = post['cmbExisteConstru']
        id_enuso = post['cmbExisteEnUso']

        item = {}
        listado = {}

        # detecta si el botón guardar fue presionado
        if 'btnGuardar' in post:
            # Si id es menor que  1, es nueva información (INSERT)
            # caso contrario lo modifica
            if id < 1:  # Valida si el usuario tiene permiso para añadir información a la tabla
                try:
                    TE.objects.create(
                        fecha_carga_ter_id=fecha,
                        ubicacion_ter_id=bip,
                        m2_inscripcion_ter=m2,
                        estadodiseno_ter_id=estado,
                        riesgo_intrusion_ter_id=id_intrusion,
                        riesgo_incendio_ter_id=id_incendio,

                        existe_gasto_ter_id=id_gasto,
                        existe_guaria_ter_id=id_guardia,
                        existe_constru_ter_id=id_constru,
                        existe_enuso_ter_id=id_enuso
                        )

                    aviso = 'Registrando datos'
                except:
                    aviso = 'ya se encuentra registrado' + str(id) + '/' +fecha+ '/'+ bip
            elif id > 0:

                item = TE.objects.get(id_eval_terrenos=id)
                item.fecha_carga_ter_id = fecha
                item.id_ubicacion = bip
                item.m2_inscripcion_ter = m2
                item.estadodiseno_ter_id = estado
                item.riesgo_intrusion_ter_id = id_intrusion
                item.riesgo_incendio_ter_id = id_incendio
                item.existe_gasto_ter_id = id_gasto
                item.existe_guaria_ter_id = id_guardia
                item.existe_constru_ter_id = id_constru
                item.existe_enuso_ter_id = id_enuso

                item.save()
                aviso = 'Registrando datos'

        elif 'btnEliminar' in post:
            item = TE.objects.get(id_eval_terrenos=id)
            item.delete()
            aviso = 'Eliminando el registro'
            item = {}

        elif 'btnListar' in post:
            listado = TE.objects.all()
            aviso = 'Listando el registro'

        # genera contexto y envia a la plantilla
        contexto = {'item': item, 'listado': listado, 'terreno': terreno, 'aviso': aviso, 'existe': existe,
                    'riesgo': riesgo, 'estadodiseno': estadodiseno, 'ubicacion': ubicacion, 'periodo': periodo}

    else:
        contexto = {'terreno': terreno, 'existe': existe, 'riesgo': riesgo, 'estadodiseno': estadodiseno,
                    'ubicacion': ubicacion, 'periodo': periodo}
    # renderiza respuesta usando plantilla y contexto
    return render(request, 'crud_eval_terrenos.html', contexto)


# genera contexto y envia a la plantilla

def CrudTerrenoRead(request, buscarId):
    item = TE.objects.get(pk=buscarId)
    ubicacion = UB.objects.all()
    existe = EX.objects.all()
    riesgo = RI.objects.all()
    estadodiseno = ED.objects.all()
    periodo = PER.objects.all()
    contexto = {'item': item, 'existe': existe, 'riesgo': riesgo, 'estadodiseno': estadodiseno,'ubicacion': ubicacion, 'periodo': periodo}
    #contexto = {'item': item}
    return render(request, 'crud_eval_terrenos.html', contexto)


def CrudPeriodoCarga(request):
    aviso = ''
    periodo = ''
    # Detecta si haay una petición

    if request.method == "POST":
        post = request.POST
        id = int('0' + post['txt_id_per'])
        fecha = post['txt_fecha_per']
        nombre = post['txt_nombre_per']

        item = {}
        listado = {}

        # detecta si el botón guardar fue presionado
        if 'btnGuardar' in post:
            # Si id es menor que  1, es nueva información (INSERT)
            # caso contrario lo modifica
            if id < 1:  # Valida si el usuario tiene permiso para añadir información a la tabla
                try:
                    PER.objects.create(fecha_per=fecha,
                                      nombre_per=nombre)

                    aviso = 'Registrando datos'
                except:
                    aviso = 'ya se encuentra registrado'

            elif id > 0:
                item = PER.objects.get(id_periodo=id)
                item.fecha_per = fecha
                item.nombre_per = nombre

                item.save()

                aviso = 'Registrando datos'

        elif 'btnEliminar' in post:
            item = PER.objects.get(id_periodo=id)
            item.delete()
            aviso = 'Eliminando el registro'
            item = {}

        elif 'btnListar' in post:
            listado = PER.objects.all()

        contexto = {'item': item, 'listado': listado, 'periodo': periodo, 'aviso': aviso, }
    else:
        contexto = {'periodo': periodo}
    # renderiza respuesta usando plantilla y contexto

    return render(request, 'crud_periodoCarga.html', contexto)


def CrudPeriodoCargaRead(request, buscarId):
    item = PER.objects.get(pk=buscarId)

    contexto = {'item': item}
    return render(request, 'crud_periodoCarga.html', contexto)
# -------------------------------API---------------------------

class CorteList(generics.ListCreateAPIView):
    queryset = CO.objects.all()
    serializer_class = CorteSerializer


class ExisteList(generics.ListCreateAPIView):
    queryset = EX.objects.all()
    serializer_class = ExisteSerializer


class UbicacionList(generics.ListCreateAPIView):
    queryset = UB.objects.all()
    serializer_class = UbicacionSerializer
