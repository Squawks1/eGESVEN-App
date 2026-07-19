from django.shortcuts import render

def inicio(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def registro(request):
    return render(request, 'registro.html')


def productos(request):
    return render(request, 'productos.html')


def detalle_producto(request):
    return render(request, 'detalle_producto.html')


def carrito(request):
    return render(request, 'carrito.html')


def checkout(request):
    return render(request, 'checkout.html')


def compra_exitosa(request):
    return render(request, 'compra_exitosa.html')


def pedidos(request):
    return render(request, 'pedidos.html')


def estado_pedido(request):
    return render(request, 'estado_pedido.html')


def admin_panel(request):
    return render(request, 'admin_panel.html')


def admin_productos(request):
    return render(request, 'admin_productos.html')


def admin_pedidos(request):
    return render(request, 'admin_pedidos.html')