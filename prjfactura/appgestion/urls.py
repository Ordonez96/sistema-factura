#urls de la app 

from .import views
from django.urls import path

urlpatterns = [
    path('', views.home_view, name='home'),
    path('clientes/', views.lista_clientes, name="lista_clientes"),
    path('clientes/nuevo/', views.crear_cliente, name="crear_cliente"),
    path('productos/', views.lista_productos, name="lista_productos"),
    path('productos/nuevo/', views.crear_producto, name="crear_producto"),
    path('facturas/', views.listar_facturas, name="lista_facturas"),
    path('facturas/nueva/', views.crear_factura, name="crear_factura"),
    path('facturas/<int:factura_id>/detalle/', views.crear_detalle_factura, name="crear_detalle_factura"),
    
]