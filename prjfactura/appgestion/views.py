from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def home_view(request):
    return render(request, 'base.html')

def crear_cliente(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'crear_cliente.html', {'form': form})

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'lista_clientes.html', {'clientes': clientes})


def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'crear_producto.html', {'form': form})

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

def crear_factura(request):
    if request.method == 'POST':
        print('post recibido')
        form_factura = FacturaForm(request.POST)
        if form_factura.is_valid():
            factura = form_factura.save()
            return redirect('crear_detalle_factura', factura_id=factura.id)
    else:
        form_factura = FacturaForm()
    return render(request, 'crear_factura.html', {'form': form_factura})

def crear_detalle_factura(request, factura_id):
    factura = Factura.objects.get(id=factura_id)
    if request.method == 'POST':
        print('post recibido')
        
        form = DetalleFacturaForm(request.POST)
        if form.is_valid():
            detalle = form.save(commit=False)
            detalle.factura = factura
            detalle.save()
            return redirect('crear_detalle_factura', factura_id=factura.id)
    else:
        form = DetalleFacturaForm()
    return render(request, 'crear_detalle_factura.html', {'form': form, 'factura': factura})

def listar_facturas(request):
    facturas = Factura.objects.all() 
    return render(request, 'listar_facturas.html', {'facturas': facturas})
