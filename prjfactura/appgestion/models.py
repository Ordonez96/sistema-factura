#models de facturacion

from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    color = models.CharField(max_length=50 , blank=True, null=True) 
    estado = models.CharField(max_length=50 , blank=True, null=True )

    def __str__(self):
        return self.nombre
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=150)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    edad = models.IntegerField( blank=True, null=True )
    
    def __str__(self):
        return self.nombre

class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Factura {self.id} - {self.cliente.nombre}"


class DetalleFactura(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField( blank=True, null=True )
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    tienda = models.CharField(max_length=150 , blank=True, null=True )
    
    @property
    def subtotal(self):
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return f' {self.cantidad} - {self.producto.nombre}'