from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
#from chilestay.views import index
from .models import Usuario, Comuna,Region
from .form import CrearUsuarioForm #InmuebleForm #ActualizarUsuarioForm, InmuebleForm, UsuarioForm, SolicitudArriendoForm
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

def hosting(request):
    return render(request, 'hosting.html')

def estadias(request):
    return render(request, 'estadias.html')

def anuncios(request):
    return render(request, 'anuncios.html')

def inmueblestodos(request):
    return render(request, 'inmueblestodos.html')

def inmueblestodos(request):
    return render(request, 'registerinmuebles.html')

def index(request):
    regiones = Region.objects.all()
    return render(request, 'index.html', {'regiones': regiones})

# Formulario de registro
def register(request):
    if request.method == 'POST':
        form = CrearUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu cuenta fue creada con éxito.')
            return redirect('login')
    else:
        form = CrearUsuarioForm()
    return render(request, 'registration/register.html', {'form': form})


@csrf_exempt
def filtrar_comunas(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            regionId = data.get('regionId')
            print('Region ID:', regionId) # Verifica el ID de la región recibida
            comunas = list(Comuna.objects.filter(region_id=regionId).values('id', 'name'))
            print('Comunas:', comunas) # Verifica las comunas filtradas
            return JsonResponse({'status': 200, 'data': comunas})
        else:
            return JsonResponse({'error': 'Método no permitido'}, status=405)
    except Exception as e:
        print('Error:', e) # Verifica los errores
        return JsonResponse({'error': str(e)}, status=400)























# @csrf_exempt
# def filtrar_comunas(request):
#     try:
#         if request.method == 'POST':
#             data = json.loads(request.body)
#             regionId = data.get('regionId')
#             print('Region ID:', regionId) # Agrega esto para verificar el ID de la región recibida
#             dataBD = list(Comuna.objects.filter(region_id=regionId).values('id', 'name'))
#             print('Comunas:', dataBD) # Agrega esto para verificar las comunas filtradas
#             return JsonResponse({'status': 200, 'data': dataBD})
#         else:
#             return JsonResponse({'error': 'Método no permitido'}, status=405)
#     except Exception as e:
#         print('Error:', e) # Agrega esto para verificar los errores
#         return JsonResponse({'error': str(e)}, status=400)













# @csrf_exempt
# def filtrar_comunas(request):
#     try:
#         if request.method == 'POST':
#             data = json.loads(request.body)
#             regionId = data.get('regionId')
#             # Filtra las comunas basadas en el regionId
#             dataBD = list(Comuna.objects.filter(region_id=regionId).values('id', 'name'))
#             return JsonResponse({'status': 200, 'data': dataBD})
#         else:
#             return JsonResponse({'error': 'Método no permitido'}, status=405)
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=400)
        









# def filtrar_comunas(request):
#     try:
#         if request.method == 'POST':
#             data = json.loads(request.body)
#             regionId = data.get('regionId')
#             print('**** region id ****', regionId)
#             dataBD = list(Comuna.objects.filter(region=regionId).values())
#             print('**** dataBD ****', dataBD)
#             return JsonResponse({'status': 200, 'data': dataBD})
#         else:
#             return JsonResponse({'error': 'Método no permitido'}, status=405)
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=400)
    
# REGISTER INMUEBLES

# @login_required
# def registerinmueble(request):
#     if not request.user.usuario.tipo_usuario == 'anfitrion':
#         return redirect('index')

#     if request.method == 'POST':
#         form = InmuebleForm(request.POST, request.FILES)
#         if form.is_valid():
#             inmueble = form.save(commit=False)
#             inmueble.anfitrion = request.user.usuario
#             inmueble.save()
#             messages.success(request, 'Inmueble agregado exitosamente')
#             return redirect('mis_inmuebles')
#     else:
#         form = InmuebleForm()
    
#     regiones = Region.objects.all()
#     return render(request, 'registerinmuebles.html', {'form': form, 'regiones': regiones})

# @login_required
# def #mis_inmuebles(request):
#     inmuebles = Inmueble.objects.filter(anfitrion=request.user.usuario)
#     return render(request, 'mis_inmuebles.html', {'inmuebles': inmuebles})