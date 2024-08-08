from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib import messages
from django.shortcuts import render
#from chilestay.views import index
from .models import Usuario #Inmueble, Region, Comuna, SolicitudArriendo
from .form import CrearUsuarioForm #ActualizarUsuarioForm, InmuebleForm, UsuarioForm, SolicitudArriendoForm
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.

#from .models import Flan #Cafe, ContactForm
#from .forms import ContactoFormForm
#from django.contrib.auth.decorators import login_required
def index(request):
    # lógica para la vista
    return render(request, 'index.html')

def hoy(request):
    return render(request, 'hoy.html')

def calendario(request):
    return render(request, 'calendario.html')

def reservaciones(request):
    return render(request, 'reservaciones.html')

def modoanfitrion(request):
    return render(request, 'modoanfitrion.html')

# Formulario de registro
def register(request):
    if request.method == 'POST':
        form = CrearUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu cuenta fue creada con éxito. Ahora puedes iniciar sesión')
            return redirect('login')
    else:
        form = CrearUsuarioForm()
    return render(request, 'registration/register.html', {'form': form})