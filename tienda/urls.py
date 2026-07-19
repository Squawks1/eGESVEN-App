from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
    path('productos/', views.productos, name='productos'),
    path('producto/', views.detalle_producto, name='detalle_producto'),
    path('carrito/', views.carrito, name='carrito'),
    path('checkout/', views.checkout, name='checkout'),
    path('compra-exitosa/', views.compra_exitosa, name='compra_exitosa'),
    path('pedidos/', views.pedidos, name='pedidos'),
    path('estado-pedido/', views.estado_pedido, name='estado_pedido'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('admin-productos/', views.admin_productos, name='admin_productos'),
    path('admin-pedidos/', views.admin_pedidos, name='admin_pedidos'),
]