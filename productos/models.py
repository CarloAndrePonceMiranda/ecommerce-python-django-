import random
import os
from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from django.urls import reverse


# Create your models here.
def get_filename_ext(filepath):
    nombre_base = os.path.basename(filepath)
    nombre, ext = os.path.splitext(nombre_base)
    return nombre, ext


def upload_image_path(instancia, nombrearchivo):
    # print(instancia)
    # print(nombrearchivo)
    nuevo_nombrearchivo = random.randint(1,3910209312)
    nombre, ext = get_filename_ext(nombrearchivo)
    nombrearchivo_final = '{nuevo_nombrearchivo}{ext}'.format(nuevo_nombrearchivo=nuevo_nombrearchivo,ext=ext)
    return "productos/{nuevo_nombrearchivo}/{nombrearchivo_final}".format(
            nuevo_nombrearchivo=nuevo_nombrearchivo,
            nombrearchivo_final=nombrearchivo_final
            )

class ProductoQuerySet(models.query.QuerySet):
    def activo(self):
        return self.filter(activo=True)

    def destacado(self):
        return self.filter(destacado=True, activo=True)

class ManejadorProducto(models.Manager):
    def get_queryset(self):
        return ProductoQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().activo()

    def destacado(self): # Producto.objects.destacado()
        return self.get_queryset().destacado()

    def get_by_id(self,id):
        qs = self.get_queryset().filter(id=id) # Producto.objects == self.get_queryset()
        if qs.count()==1:
            return qs.first()
        return None


class Producto(models.Model):
    nombre      = models.CharField(max_length=120)
    marcado     = models.SlugField(blank=True, unique=True)
    descripcion = models.TextField()
    precio      = models.DecimalField(decimal_places=2, max_digits=20, default=49.99)
    imagen      = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    destacado   = models.BooleanField(default=False)
    activo      = models.BooleanField(default=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = ManejadorProducto()
    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        # return "/productos/{marcado}/".format(marcado=self.marcado)
        return reverse("productos:detalle", kwargs={"marcado": self.marcado})


def producto_pre_guardado_recividor(sender, instance, *arg, **kwargs):
    if not instance.marcado:
        instance.marcado = unique_slug_generator(instance)

pre_save.connect(producto_pre_guardado_recividor, sender=Producto)
