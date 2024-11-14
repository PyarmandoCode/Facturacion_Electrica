from django.db import models
from django.contrib.auth.models import User


class Contacto(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    nomcompleto = models.CharField(max_length=400)
    nombreabrev = models.CharField(max_length=20)
    email=models.CharField(max_length=100, blank=True, null=True)
    direccion=models.CharField(max_length=150, blank=True, null=True)
    telefono=models.CharField(max_length=100, blank=True, null=True)
    state = models.BooleanField(default=True)

    class Meta:
        db_table = 'Contacto'

    def __str__(self):
        return self.nombre 



class Empresa (models.Model):
    nombre = models.CharField(max_length=200)
    #Esto es el RUC
    cedula=models.CharField(max_length=20)
    email = models.EmailField(blank=True,null=True)
    logo_path=models.CharField(max_length=400,blank=True,null=True)
    direccion=models.CharField(max_length=250)
    telefono = models.CharField(max_length=10)
    contacto = models.ForeignKey(Contacto,models.DO_NOTHING)
    #1 activa
    #0 desactiva
    fecha_creacion  = models.DateTimeField()
    usuario = models.ForeignKey(User, models.DO_NOTHING)
    state = models.BooleanField(default=True)
    

    class Meta:
        db_table = 'Empresa'

    def __str__(self):
        return self.nombre    
    
class Categoria (models.Model):
    nombre = models.CharField(max_length=200)
    logo_categoria=models.CharField(max_length=400,blank=True,null=True)
    fecha_creacion  = models.DateTimeField()
    usuario = models.ForeignKey(User, models.DO_NOTHING)
    state = models.BooleanField(default=True)
    

    class Meta:
        db_table = 'Categoria'

    def __str__(self):
        return self.nombre  
    
# class Factores(models.Model):
#     nombre = models.CharField(max_length=200)
#     fecha_creacion  = models.DateTimeField()
#     usuario = models.ForeignKey(User, models.DO_NOTHING)
#     state = models.BooleanField(default=True) 

#     class Meta:
#         db_table = 'Factores'

#     def __str__(self):
#         return self.nombre    
    
class Umedida (models.Model):
    nombre = models.CharField(max_length=200)
    fecha_creacion  = models.DateTimeField()
    usuario = models.ForeignKey(User, models.DO_NOTHING)
    state = models.BooleanField(default=True)
    

    class Meta:
        db_table = 'Umedida'

    def __str__(self):
        return self.nombre  

class Proveedor (models.Model):
    nombre = models.CharField(max_length=200)
    cedula = models.CharField(max_length=20)
    direccion=models.CharField(max_length=150, blank=True, null=True)
    email=models.CharField(max_length=100, blank=True, null=True)
    telefono=models.CharField(max_length=100, blank=True, null=True)
    fecha_creacion  = models.DateTimeField()
    empresa=models.ForeignKey(Empresa, models.DO_NOTHING)
    usuario = models.ForeignKey(User, models.DO_NOTHING)
    state = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'Proveedor'

    def __str__(self):
        return self.nombre    
    

class Productos(models.Model):
    #Relacionado con la hacienda o sunat
    #codbarra=models.ForeignKey(CodigosBarra, models.DO_NOTHING)
    codcabys= models.CharField(max_length=255)
    nombre=models.CharField(max_length=255)
    categoria=models.ForeignKey(Categoria, models.DO_NOTHING,blank=True, null=True)
    proveedor=models.ForeignKey(Proveedor, models.DO_NOTHING)
    descripcion=models.TextField(blank=True, null=True)
    precio_real=models.DecimalField(max_digits=7,decimal_places=2)
    precio_ofrecido=models.DecimalField(max_digits=7,decimal_places=2)
    umedida=models.ForeignKey(Umedida, models.DO_NOTHING)
    empresa=models.ForeignKey(Empresa, models.DO_NOTHING)
    logo_producto = models.CharField(max_length=400,blank=True,null=True)
    fecha_creacion  = models.DateTimeField()
    usuario = models.ForeignKey(User, models.DO_NOTHING)
    state = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'Producto'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
    
class CodigosBarra(models.Model):
    codigo = models.CharField(max_length=255)
    producto = models.ForeignKey(Productos, models.DO_NOTHING,null=True,blank=True)
    fecha_creacion  = models.DateTimeField()
    usuario = models.ForeignKey(User, models.DO_NOTHING)
    state = models.BooleanField(default=True)
    

    class Meta:
        db_table = 'CodigosBarra'

    def __str__(self):
        return f"Barra:{self.codigo} del Producto:{self.producto.nombre}"      

# class Inventario(models.Model):
#     empresa = models.ForeignKey(Empresa, models.DO_NOTHING)
#     producto = models.ForeignKey(Productos, models.DO_NOTHING)
#     cantidad = models.IntegerField()
#     fecha_creacion  = models.DateTimeField()
#     usuario = models.ForeignKey(User, models.DO_NOTHING)
#     state = models.BooleanField(default=True)

#     class Meta:
#         db_table = 'Inventario'
       
#     def __str__(self):
#         return self. empresa
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    cedula = models.CharField(max_length=20)
    direccion=models.CharField(max_length=150, blank=True, null=True)
    email=models.CharField(max_length=100, blank=True, null=True)
    telefono=models.CharField(max_length=100, blank=True, null=True)
    empresa=models.ForeignKey(Empresa, models.DO_NOTHING,blank=True, null=True)
    fecha_creacion  = models.DateTimeField(blank=True, null=True)
    usuario = models.ForeignKey(User, models.DO_NOTHING,blank=True, null=True)
    state = models.BooleanField(default=True,blank=True, null=True)

    class Meta:
        db_table = 'Cliente'

    def __str__(self):
        return self.nombre      


class FacturaCabecera(models.Model):
    nrofactura=models.CharField(max_length=8,primary_key=True)
    cliente=models.ForeignKey(Cliente, models.DO_NOTHING)
    fecha_factura=models.DateField(blank=True, null=True)
    usuario = models.ForeignKey(User, models.DO_NOTHING)
    empresa=models.ForeignKey(Empresa, models.DO_NOTHING)
    con_sin_igv=models.BooleanField()
    descuento =models.DecimalField(max_digits=7,decimal_places=2)
    impuesto=models.DecimalField(max_digits=7,decimal_places=2)
    state = models.BooleanField(default=True)

    class Meta:
        db_table = 'FacturaCabecera'
        

    def __str__(self):
        return self.nrofactura
    
class FacturaDetalle(models.Model):
    factura = models.ForeignKey(FacturaCabecera, models.DO_NOTHING)
    productos = models.ForeignKey(Productos, models.DO_NOTHING)
    cantidad = models.IntegerField()
    descuento =models.DecimalField(max_digits=7,decimal_places=2)

    class Meta:
        db_table = 'FacturaDetalle'
        

    def __str__(self):
        return self.factura

        


