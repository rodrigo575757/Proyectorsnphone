from django.db import models

# Create your models here.
class Raza(models.Model):
    codigo = models.AutoField(primary_key=True,verbose_name='Código de la raza')
    nombreRaza = models.CharField(null=True, max_length=25,verbose_name='Nombre de la raza', blank=True)

class Mascota(models.Model):
    codigoChip = models.IntegerField(primary_key=True)
    nombreMascota = models.CharField(max_length=30)
    edadMascota = models.IntegerField()
    foto = models.ImageField(upload_to="mascotas")
    raza = models.ForeignKey(Raza,on_delete=models.CASCADE)


class USUARIO(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    correo = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)

class ROL(models.Model): 
    id_rol = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)

class VENTA(models.Model):
    id_venta = models.IntegerField(primary_key=True)
    fecha_venta = models.DateField()
    total = models.IntegerField()
    estado = models.CharField(max_length=20)
    carrito = models.IntegerField()

class DETALLE_VENTA(models.Model):  
    id_detalle = models.IntegerField(primary_key=True)   
    cantidad = models.IntegerField()
    subtotal = models.IntegerField()

class PRODUCTO(models.Model):
    id_producto = models.IntegerField(primary_key=True)   
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=300)
    precio = models.ImageField()
    stock = models.ImageField()
    foto = models.ImageField(upload_to="Inicioproject")

class MARCA(models.Model):
    id_marca = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)

class SUCURSAL(models.Model):
    id_sucursal = models.IntegerField(primary_key=True) 
    nombre = models.CharField(max_length=30)

class DIRECCION(models.Model):
    id_direccion = models.IntegerField(primary_key=True)
    calle = models.CharField(max_length=30) 
    numero_c = models.ImageField()

class COMUNA(models.Model):  
    id_comuna = models.IntegerField(primary_key=True)   
    nombre = models.CharField(max_length=30) 

class REGION(models.Model):
    id_region = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)  



    
