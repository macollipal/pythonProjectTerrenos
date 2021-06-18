from django.db import models

# Create your models here.
from datetime import date


class Existe(models.Model):
    id_existe = models.AutoField(primary_key=True)
    nombre_exi = models.CharField(max_length=20, verbose_name='Existe')
    valor_exi = models.IntegerField(default=0, verbose_name='Valor')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f' {self.nombre_exi}, {self.valor_exi}'


class Riesgo(models.Model):
    id_riesgo = models.AutoField(primary_key=True)
    nombre_rie = models.CharField(max_length=20, verbose_name='Riesgo')
    valor_rie = models.IntegerField(default=0, verbose_name='Valor')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f' {self.nombre_rie}, {self.valor_rie}'


class EstadoDiseno(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nombre_est = models.CharField(max_length=100, verbose_name='Estado Diseño')
    valor_est = models.IntegerField(default=0, verbose_name='Valor Estado')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f' {self.id_estado},{self.nombre_est}'


class TipoCierre(models.Model):
    id_tcierre = models.AutoField(primary_key=True)
    nombre_tci = models.CharField(max_length=100, verbose_name='Tipo Cierre')
    valor_tci = models.IntegerField(default=0, verbose_name='Valor TipoCierre')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f' {self.nombre_est},{self.valor_est}'


class Corte(models.Model):
    id_corte = models.AutoField(primary_key=True)
    nombre_cor = models.CharField(max_length=100, verbose_name='Corte')
    descripcion_cor = models.CharField(max_length=100, blank=True, verbose_name='Descripcion')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f' {self.id_corte}, {self.nombre_cor}'


class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre_com = models.CharField(max_length=100, verbose_name='Comuna')
    zona_com = models.CharField(max_length=100, blank=True, verbose_name='Zona')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f' {self.nombre_com},{self.zona_com}'


class Ubicacion(models.Model):
    id_ubicacion = models.AutoField(primary_key=True)
    bip_ubi = models.CharField(max_length=8, blank=True, verbose_name='BIP')
    corte_ubi = models.ForeignKey(Corte, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Corte')
    comuna_ubi = models.ForeignKey(Comuna, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Comuna')
    direccion_ubi = models.CharField(max_length=100, blank=True, verbose_name='Direccion')
    latitud_ubi = models.IntegerField(blank=False, null=True, verbose_name='Latitud')
    longitud_ubi = models.IntegerField(blank=False, null=True, verbose_name='Longitud')
    unidad_destino_ubi = models.CharField(max_length=100, blank=True, verbose_name='Unidad Destino')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f' {self.bip_ubi}, {self.corte_ubi}, {self.comuna_ubi}, {self.direccion_ubi}, {self.latitud_ubi}, {self.longitud_ubi}, {self.unidad_destino_ubi}'

class PeriodoCarga(models.Model):
    id_periodo = models.AutoField(primary_key=True)
    fecha_per = models.DateField(auto_now=False, verbose_name = 'Fecha Periodo Carga')
    nombre_per =models.CharField(max_length=100, blank=True, verbose_name = 'Periodo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f' {self.id_periodo},{self.fecha_per}, {self.nombre_per}'

class Eval_Terrenos(models.Model):
    id_eval_terrenos = models.AutoField(primary_key=True)
    fecha_carga_ter = models.ForeignKey(PeriodoCarga, blank=True, null=True, on_delete=models.SET_NULL)
    ubicacion_ter = models.ForeignKey(Ubicacion, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='BIP')
    m2_inscripcion_ter = models.IntegerField(blank=True, null=True, default=0,  verbose_name='M2')
    estadodiseno_ter = models.ForeignKey(EstadoDiseno, blank=True, null=True, on_delete=models.SET_NULL,
                                         related_name='estadodiseno', verbose_name='Estado Diseño')
    fecha_ini_diseno_ter = models.DateField(null=True, verbose_name='Fecha Inicio Diseño')
    fecha_constru_ter = models.DateField(null=True, verbose_name='Fecha Construccion')
    fecha_entrega_ter = models.DateField(null=True, verbose_name='Fecha Entrega')

    riesgo_intrusion_ter = models.ForeignKey(Riesgo, blank=True, null=True, on_delete=models.SET_NULL,
                                             related_name='Intrusion', verbose_name='Riesgo Intrusion')
    riesgo_incendio_ter = models.ForeignKey(Riesgo, blank=True, null=True, on_delete=models.SET_NULL,
                                            related_name='Incendio', verbose_name='Riesgo Incendio')

    existe_gasto_ter = models.ForeignKey(Existe, blank=True, null=True, on_delete=models.SET_NULL,
                                         related_name='ExisteGasto', verbose_name='Existe Gasto')
    existe_guaria_ter = models.ForeignKey(Existe, blank=True, null=True, on_delete=models.SET_NULL,
                                          related_name='ExisteGuardia', verbose_name='Existe Guardia')
    existe_constru_ter = models.ForeignKey(Existe, blank=True, null=True, on_delete=models.SET_NULL,
                                           related_name='ExisteConstru', verbose_name='Existe Construccion')
    existe_enuso_ter = models.ForeignKey(Existe, blank=True, null=True, on_delete=models.SET_NULL,
                                         related_name='ExisteEnUso', verbose_name='Existe En Uso')
    fecha_compra_ter = models.DateField(null=True, verbose_name='Fecha Compra')
    monto_uf_ter = models.IntegerField(blank=True, null=True, verbose_name='Monto UF')
    obs_ter = models.CharField(max_length=100, blank=True, verbose_name='Observacion')
    kpi = models.DecimalField(max_digits=6, decimal_places=2,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(editable=False, auto_now=True)

    def __str__(self):
        return f' {self.id_eval_terrenos}, {self.fecha_carga_ter}, {self.ubicacion_ter}, {self.m2_inscripcion_ter},' \
               f' {self.estadodiseno_ter}, {self.fecha_ini_diseno_ter}, {self.fecha_constru_ter} , {self.fecha_entrega_ter},' \
               f' {self.riesgo_intrusion_ter}, {self.riesgo_incendio_ter}, {self.existe_gasto_ter} , {self.existe_guaria_ter},' \
               f' {self.existe_constru_ter}, {self.existe_enuso_ter}, {self.fecha_compra_ter} , {self.monto_uf_ter}, {self.obs_ter}'
