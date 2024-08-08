from django.shortcuts import get_object_or_404
from .models import Usuario
#Region, Comuna, TipoInmueble, Inmueble, SolicitudArriendo

# Crear un objeto con el modelo Usuario
def crear_usuario(user, rut, direccion, telefono, correo_electronico, tipo_usuario='huesped'):
    #nombres, apellidos,
    
    usuario = Usuario(
        user=user,
        #nombres=nombres,
        #apellidos=apellidos,
        rut=rut,
        direccion=direccion,
        telefono=telefono,
        correo_electronico=correo_electronico,
        tipo_usuario=tipo_usuario
    )
    usuario.save()
    return usuario

