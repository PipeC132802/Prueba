from django.db import models


# Create your models here.
class Compradores(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=20)
    longitud = models.CharField(max_length=20, blank=True, null=True)
    latitud = models.CharField(max_length=20, blank=True, null=True)
    estado_geo = models.BooleanField(default=False)

    def serializer(self):
        return {
            'id': self.pk,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'ciudad': self.ciudad,
            'longitud': self.longitud,
            'latitud': self.latitud,
            'estado_geo': self.estado_geo
        }

    def __str__(self):
        return '{0} {1}, estado_geo: {2}'.format(self.nombre, self.apellido, self.estado_geo)
