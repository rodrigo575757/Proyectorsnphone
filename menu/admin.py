from django.contrib import admin
from .models import Usuario, Rol, Venta, Detalle_venta, Producto, Marca, Sucursal, Direccion, Comuna, Region

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Rol)
admin.site.register(Venta)
admin.site.register(Detalle_venta)
admin.site.register(Producto)
admin.site.register(Marca)
admin.site.register(Sucursal)
admin.site.register(Direccion)
admin.site.register(Comuna)
admin.site.register(Region)