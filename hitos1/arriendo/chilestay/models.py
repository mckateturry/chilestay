from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pais(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    name_en= models.CharField(max_length=50, null=True, blank=True)
    def __str__(self) -> str:
        return f"({self.id}) - {self.name}"
    
class Region(models.Model):
    name= models.CharField(max_length=50, null=False, blank=False)
    pais = models.ForeignKey(Pais,null=False, blank=False, on_delete= models.CASCADE ) #FK uno a muchos
    def __str__(self) -> str:
        return f"({self.id}) - {self.name}"
    
class Comuna(models.Model):
    name= models.CharField(max_length=50, null=False, blank=False)
    region = models.ForeignKey(Region, null=False, blank=False, on_delete=models.CASCADE ) #FK uno a muchos
    def __str__(self) -> str:
        return f"({self.id}) - {self.name} - region: {self.region.name}"

class TipoUsuario(models.Model):
    nombre= models.CharField(max_length=20, null=False, blank=False)
    descripcion= models.CharField(max_length=40, null=False, blank=False)
    def __str__(self) -> str:
        return f"({self.id}) - {self.nombre}"
    
class Usuario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rut= models.CharField()
    direccion= models.CharField()
    telefono= models.CharField()
    tipo_usuario = models.ForeignKey(TipoUsuario, null=False, blank=False, on_delete= models.CASCADE ) #FK uno a muchos
    def __str__(self) -> str:
        return f"({self.id}) - {self.user.first_name}"
    
class TipoInmueble(models.Model):
    nombre= models.CharField(max_length=25, null=False, blank=False)
    def __str__(self) -> str:
        return f"({self.id}) - {self.nombre}"
    
class Inmueble(models.Model):
    nombre= models.CharField(max_length=25, null=False, blank=False)
    #anfitrion= models.OneToOneField(User,null=False) #ofrece
    #huesped= models.OneToOneField(Usuario,null=True) #paga
    arrendada= models.BooleanField(default=False)
    comuna= models.ForeignKey(Comuna, on_delete=models.CASCADE, null=False, blank=False)
    region= models.ForeignKey(Region, on_delete=models.CASCADE, null=False, blank=False)
    tipo_inmueble= models.ForeignKey(TipoInmueble,on_delete= models.CASCADE, null=False, blank=False)
    
    usuarios= models.ManyToManyField(Usuario, related_name='inmuebles')
    
    def __str__(self) -> str:
        return f"({self.id}) - {self.nombre}"
    
'''
#tabla relacional Mucho a Mucho, para agregar campos extras
class InmuebleUsuario(models.Model):
pass
'''