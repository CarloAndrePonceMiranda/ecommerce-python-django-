"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib.auth import views
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin

from productos.views import (
#         ListaProducto,
#         lista_producto,
        ListaProductoDestacado,
#         ###########
#         DetalleProducto,
#         detalle_producto,
#         DetalleProductoDestacado,
#         ###########
#         DetalleProductoMarcado
         )

from .views import home_page, contact_page, about_page, login_page, logout, register_page



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page,name='home'),
    url(r'^contact/$', contact_page,name='contacto'),
    url(r'^about/$', about_page,name='about'),
    url(r'^login/$', login_page,name='login'),
    url(r'^register/$', register_page,name='register'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),

    url(r'^productos/',include("productos.urls",namespace='productos')),

    # url(r'^productos/$', ListaProducto.as_view()),
    # url(r'^productos-fbv/$', lista_producto),
    url(r'^destacados/$', ListaProductoDestacado.as_view(),name='destacados'),
    # # url(r'^productos/(?P<pk>\d+)/$', DetalleProducto.as_view()),
    # url(r'^productos-fbv/(?P<pk>\d+)/$', detalle_producto),
    # url(r'^destacados/(?P<pk>\d+)/$', DetalleProductoDestacado.as_view()),
    # url(r'^productos/(?P<marcado>[\w-]+)/$', DetalleProductoMarcado.as_view()),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
