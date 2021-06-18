from rest_framework import serializers
from crud.models import Corte, Existe, Ubicacion


class CorteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corte
        fields = ('id_corte','nombre_cor', 'descripcion_cor')

class ExisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Existe
        fields = ('id_existe','nombre_exi', 'valor_exi')

class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = ('id_ubicacion','bip_ubi', 'direccion_ubi','comuna_ubi_id','corte_ubi_id','latitud_ubi','longitud_ubi','unidad_destino_ubi')
