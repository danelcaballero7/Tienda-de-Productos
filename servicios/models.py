from django.db import models


# Create your models here.
class Servicio(models.Model):
    titulo = models.CharField(max_length=50, verbose_name='Titulo')
    contenido = models.CharField(max_length=60, verbose_name='Contenido')
    imagen = models.ImageField(upload_to='servicios', verbose_name='Imagen')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de actualizacion')


    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    def __str__(self):
        return self.titulo
