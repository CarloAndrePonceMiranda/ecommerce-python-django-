from django.conf.urls import url
from .views import (
        ListaProducto,
        DetalleProductoMarcado
        )



urlpatterns = [
    url(r'^$', ListaProducto.as_view(),name='lista'),
    url(r'^(?P<marcado>[\w-]+)/$', DetalleProductoMarcado.as_view(), name='detalle'),
]
