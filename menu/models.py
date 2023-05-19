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
    
