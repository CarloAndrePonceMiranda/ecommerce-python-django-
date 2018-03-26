from django.contrib import admin
from .models import Producto
# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'marcado']
    class Meta:
        model = Producto

admin.site.register(Producto, ProductoAdmin)
