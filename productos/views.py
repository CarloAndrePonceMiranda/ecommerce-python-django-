# -*- coding: utf-8 -*-
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Producto
# Create your views here.

class ListaProductoDestacado(ListView):
    template_name = "productos/lista-destacado.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Producto.objects.all().destacado()

class DetalleProductoDestacado(DetailView):
    queryset = Producto.objects.all().destacado()
    template_name = "productos/detalle-destacado.html"

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Producto.objects.destacado()



class ListaProducto(ListView):
    template_name = "productos/lista.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ListaProducto,self).get_context_data(*args,**kwargs)
    #     print(context)
    #     return context
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Producto.objects.all()

def lista_producto(request):
    queryset = Producto.objects.all()
    context = {
        'qs':queryset
    }
    return render(request, "productos/lista.html", context)


class DetalleProductoMarcado(DetailView):
    queryset = Producto.objects.all()
    template_name = "productos/detalle.html"

    def get_object(self, *args, **kwargs):
        request = self.request
        marcado = self.kwargs.get('marcado')
        # instancia = get_object_or_404(Producto, marcado=marcado, activo=True)
        try:
            instancia = Producto.objects.get(marcado=marcado, activo=True)
        except Producto.DoesNotExist:
            raise Http404("No se encuentra...")
        except Producto.MultipleObjectsReturned:
            qs = Producto.objects.filter(marcado=marcado, activo=True)
            instancia = qs.first()
        except:
            raise Http404("¡Uhhmm")
        return instancia


class DetalleProducto(DetailView):
    # queryset = Producto.objects.all()
    template_name = "productos/detalle.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DetalleProducto,self).get_context_data(*args,**kwargs)
        print(context)
        # context = ['abc'] = 123
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instancia = Producto.objects.get_by_id(pk)
        if instancia is None:
            raise Http404("¡El Producto que buscas no existe!")
        return instancia

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     return queryset = Producto.objects.filter(pk=pk)


def detalle_producto(request, pk=None, *args, **kwargs):
    instancia = Producto.objects.get(pk=pk, destacado=True)
    # instancia = get_object_or_404(Producto, pk=pk, destacado=True)
    # try:
    #     instancia = Producto.objects.get(pk=pk)
    # except Producto.DoesNotExist:
    #     print("No hay Productos aqui.")
    #     raise Http404("¡El Producto que buscas no existe!")
    # except:
    #     print("¿Huh?")
    instancia = Producto.objects.get_by_id(pk)
    if instancia is None:
        raise Http404("¡El Producto que buscas no existe!")
    # print(instancia)
    # qs = Producto.objects.filter(id=pk)
    # # print(qs)
    # if qs.exists() and qs.count() == 1: # Longitud del qs
    #     instancia = qs.first()
    # else:
    #     raise Http404("¡El Producto que buscas no existe!")
    context = {
        'object':instancia
    }
    return render(request, "productos/detalle.html", context)
