from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied

# Create your models here.
#class Pais(models.Model):
 #   name = models.CharField(max_length=50, null=False, blank=False)
  #  name_en= models.CharField(max_length=50, null=True, blank=True)
   # def __str__(self) -> str:
    #    return f"({self.id}) - {self.name}"
    
class Region(models.Model):
    
    name= models.CharField(max_length=50, null=False, blank=False)
    #pais = models.ForeignKey(Pais,null=False, blank=False, on_delete= models.CASCADE ) #FK uno a muchos
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
    correo_electronico = models.EmailField(max_length=255, default='default@example.com') 
    tipo_usuario = models.ForeignKey(TipoUsuario, null=False, blank=False, on_delete= models.CASCADE ) #FK uno a muchos
    def __str__(self) -> str:
        return f"({self.user}) {self.user.first_name}"
    
class TipoInmueble(models.Model):
    nombre= models.CharField(max_length=25, null=False, blank=False)
    def __str__(self) -> str:
        return f"({self.id}) - {self.nombre}"
    
    
class Inmueble(models.Model):
    CALIFICACIONES_SERNAUR = [
        ('sello_calidad', 'Sello de calidad turística'),
        ('sello_sustentabilidad', 'Sello de sustentabilidad turística'),
        ('compromiso_practicas', 'Compromiso buenas prácticas'),
    ]

    id = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=255)
    arrendada = models.BooleanField(default=False)
    direccion = models.CharField(max_length=255, default='Dirección por defecto')
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, null=False, blank=False)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=False, blank=False)
    tipo_inmueble = models.ForeignKey(TipoInmueble, on_delete=models.CASCADE, null=False, blank=False)
    servicios = models.JSONField(default=dict)
    calificacion_sernatur = models.JSONField(default=dict)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    correo_electronico = models.EmailField(blank=True, null=True)
    pagina_web = models.URLField(blank=True, null=True)
    descripcion = models.TextField(default='Descripción por defecto')
    usuarios = models.ManyToManyField(User, related_name='inmuebles')
    fecha_disponible_desde = models.DateField(null=True, blank=True)
    fecha_disponible_hasta = models.DateField(null=True, blank=True)
    capacidad_adultos = models.PositiveIntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Restricción para modificar CALIFICACIONES_SERNAUR solo por el creador
        if not self.pk and not self._state.adding:
            if not self._state.adding and not self.usuarios.filter(is_superuser=True).exists():
                raise PermissionDenied("No tienes permiso para modificar CALIFICACIONES_SERNAUR")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre  
    
#restablecer1
# class Inmueble(models.Model):
#     CALIFICACIONES_SERNAUR = [
#         ('sello_calidad', 'Sello de calidad turística'),
#         ('sello_sustentabilidad', 'Sello de sustentabilidad turística'),
#         ('compromiso_practicas', 'Compromiso buenas prácticas'),
#     ]

#     id = models.CharField(max_length=10, primary_key=True)
#     nombre = models.CharField(max_length=255)
#     arrendada = models.BooleanField(default=False)
#     direccion = models.CharField(max_length=255, default='Dirección por defecto') 
#     #direccion = models.CharField(max_length=255)
#     comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, null=False, blank=False)
#     region = models.ForeignKey(Region, on_delete=models.CASCADE, null=False, blank=False)
#     tipo_inmueble= models.ForeignKey(TipoInmueble,on_delete= models.CASCADE, null=False, blank=False)
#     #tipo_inmueble = models.CharField(max_length=50)
#     servicios = models.JSONField(default=dict)  
#     #servicios = models.JSONField()
#     calificacion_sernatur = models.JSONField(default=dict)  
#     telefono = models.CharField(max_length=20, blank=True, null=True)
#     correo_electronico = models.EmailField(blank=True, null=True)
#     pagina_web = models.URLField(blank=True, null=True)
#     descripcion = models.TextField(default='Descripción por defecto')  
#     usuarios = models.ManyToManyField(User, related_name='inmuebles')  

#     def __str__(self):
#         return self.nombre    
    
    
"""class Inmueble(models.Model):
    CALIFICACIONES_SERNAUR = [
        ('sello_calidad', 'Sello de calidad turística'),
        ('sello_sustentabilidad', 'Sello de sustentabilidad turística'),
        ('compromiso_practicas', 'Compromiso buenas prácticas'),
    ]

    id = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=255)
    arrendada = models.BooleanField(default=False)
    direccion = models.CharField(max_length=255)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, null=False, blank=False)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=False, blank=False)
    tipo_inmueble= models.ForeignKey(TipoInmueble,on_delete= models.CASCADE, null=False, blank=False)
    #tipo_inmueble = models.CharField(max_length=50)
    servicios = models.JSONField()
    calificacion_sernatur = models.JSONField(default=dict)  # Agregar un valor por defecto aquí
    telefono = models.CharField(max_length=20, blank=True, null=True)
    correo_electronico = models.EmailField(blank=True, null=True)
    pagina_web = models.URLField(blank=True, null=True)
    descripcion = models.TextField()
    usuarios = models.ManyToManyField(User, related_name='inmuebles')  # Asume que el modelo de usuario es User

    def __str__(self) -> str:
        return f"({self.id}) - {self.nombre}"
    #def __str__(self):
     #   return self.nombre"""

    
#class Inmueble(models.Model):
 #   nombre= models.CharField(max_length=25, null=False, blank=False)
    #anfitrion= models.OneToOneField(User,null=False) #ofrece
    #huesped= models.OneToOneField(Usuario,null=True) #paga
  #  arrendada= models.BooleanField(default=False)
   # comuna= models.ForeignKey(Comuna, on_delete=models.CASCADE, null=False, blank=False)
    #region= models.ForeignKey(Region, on_delete=models.CASCADE, null=False, blank=False)
    #tipo_inmueble= models.ForeignKey(TipoInmueble,on_delete= models.CASCADE, null=False, blank=False)
    
    #usuarios= models.ManyToManyField(Usuario, related_name='inmuebles')
    
   # def __str__(self) -> str:
    #    return f"({self.id}) - {self.nombre}"
    
'''
#tabla relacional Mucho a Mucho, para agregar campos extras
class InmuebleUsuario(models.Model):
pass
'''