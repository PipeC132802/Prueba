from rest_framework import serializers

from Apps.Compradores.models import Compradores


class CompradoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compradores
        fields = ['nombre', 'apellido', 'ciudad', 'direccion', 'longitud', 'latitud', 'estado_geo']






