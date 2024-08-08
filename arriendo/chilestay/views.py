from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib import messages
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
#from chilestay.views import index
from .models import Usuario, Comuna,Region, Inmueble
from .form import CrearUsuarioForm, ProfileForm, InmuebleForm, FiltroInmuebleForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import PermissionDenied

# Create your views here.

# def index(request):
#     form = FiltroInmuebleForm(request.GET or None)
#     inmuebles = Inmueble.objects.all()

def index(request):
    inmuebles = Inmueble.objects.all()
    zona = request.GET.get('zona')
    llegada = request.GET.get('llegada')
    salida = request.GET.get('salida')
    adultos = request.GET.get('adultos')
    ninos = request.GET.get('ninos')
    bebes = request.GET.get('bebes')
    mascotas = request.GET.get('mascotas')

    if zona:
        regiones = []
        if zona == 'norte':
            regiones = ['Arica y Parinacota', 'Tarapacá', 'Antofagasta', 'Atacama']
        elif zona == 'centro':
            regiones = ['Coquimbo', 'Valparaíso', 'Región Metropolitana de Santiago', 'Región del Libertador Gral. Bernardo O’Higgins', 'Región del Maule']
        elif zona == 'sur':
            regiones = ['Región de Ñuble', 'Región del Biobío', 'Región de la Araucanía', 'Región de Los Ríos', 'Región de Los Lagos']
        elif zona == 'austral':
            regiones = ['Región Aisén del Gral. Carlos Ibáñez del Campo', 'Región de Magallanes y de la Antártica Chilena']
        inmuebles = inmuebles.filter(region__name__in=regiones)

    if llegada:
        inmuebles = inmuebles.filter(fecha_disponible_desde__lte=llegada)

    if salida:
        inmuebles = inmuebles.filter(fecha_disponible_hasta__gte=salida)

    # Agrega otros filtros aquí según sea necesario

    context = {
        'inmuebles': inmuebles,
    }
    return render(request, 'index.html', context)




# def index(request):
#     inmuebles = Inmueble.objects.all()

#     zona = request.GET.get('zona')
#     llegada = request.GET.get('llegada')
#     salida = request.GET.get('salida')
#     adultos = request.GET.get('adultos', 0)
    
#     # Filtrar por zona
#     if 'zona' in request.GET:
#         zona = request.GET.get('zona')
#         if zona:
#             if zona == 'norte':
#                 inmuebles = inmuebles.filter(region__in=['Arica y Parinacota', 'Tarapacá', 'Antofagasta', 'Atacama'])
#             elif zona == 'centro':
#                 inmuebles = inmuebles.filter(region__in=['Coquimbo', 'Valparaíso', 'Región Metropolitana de Santiago', 'Región del Libertador Gral. Bernardo O’Higgins', 'Región del Maule'])
#             elif zona == 'sur':
#                 inmuebles = inmuebles.filter(region__in=['Región de Ñuble', 'Región del Biobío', 'Región de la Araucanía', 'Región de Los Ríos', 'Región de Los Lagos'])
#             elif zona == 'austral':
#                 inmuebles = inmuebles.filter(region__in=['Región Aisén del Gral. Carlos Ibáñez del Campo', 'Región de Magallanes y de la Antártica Chilena'])

#     # Filtrar por fechas
#     if 'llegada' in request.GET:
#         llegada = request.GET.get('llegada')
#         if llegada:
#             inmuebles = inmuebles.filter(fecha_disponible_desde__lte=llegada)

#     if 'salida' in request.GET:
#         salida = request.GET.get('salida')
#         if salida:
#             inmuebles = inmuebles.filter(fecha_disponible_hasta__gte=salida)

#     # Filtrar por capacidad
#     if 'adultos' in request.GET:
#         try:
#             adultos = int(request.GET.get('adultos', 0))
#             inmuebles = inmuebles.filter(capacidad_adultos__gte=adultos)
#         except ValueError:
#             pass  # Manejar el caso en el que 'adultos' no sea un número válido

#     return render(request, 'index.html', {'inmuebles': inmuebles})
#     # return render(request, 'index.html', {'form': form, 'inmuebles': inmuebles})


def hoy(request):
    return render(request, 'hoy.html')

def modoanfitrion(request):
    return render(request, 'modoanfitrion.html')

def modoviajero(request):
    return render(request, 'modoviajero.html')

def cuenta(request):
    return render(request, 'cuenta.html')

def viajes(request):
    return render(request, 'viajes.html')

def hosting(request):
    return render(request, 'hosting.html')

def estadias(request):
    return render(request, 'estadias.html')

def anuncios(request):
    return render(request, 'anuncios.html')


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

#EDITARPERFIL
class EditProfileView(View):
    def get(self, request):
        usuario = Usuario.objects.get(user=request.user)
        form = ProfileForm(instance=usuario)
        return render(request, 'cuentaeditar.html', {'form': form})

    def post(self, request):
        usuario = Usuario.objects.get(user=request.user)
        form = ProfileForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('cuenta')
        return render(request, 'cuentaeditar.html', {'form': form})


class CuentaView(View):
    def get(self, request):
        usuario = Usuario.objects.get(user=request.user)
        print(f"Correo Electrónico: {usuario.correo_electronico}") 
        return render(request, 'cuenta.html', {'usuario': usuario, 'user': request.user})
    

def registro_inmueble(request):
    # Lógica para registrar inmueble
    return render(request, 'registro_inmueble.html')

def inmueble_list(request):
    # Lógica para listar inmuebles
    return render(request, 'inmueble_list.html')

def calendario(request):
    # Lógica para mostrar el calendario
    return render(request, 'calendario.html')

def mensajes(request):
    # Lógica para mostrar mensajes
    return render(request, 'mensajes.html')

def reservaciones(request):
    # Lógica para mostrar reservaciones
    return render(request, 'reservaciones.html')

def estadisticas(request):
    # Lógica para mostrar estadísticas
    return render(request, 'estadisticas.html')

def solicitar_certificacion(request):
    # Lógica para solicitar certificación SERNATUR
    return render(request, 'solicitar_certificacion.html')






    
# def registro_inmueble(request):
#     if request.method == 'POST':
#         form = InmuebleForm(request.POST, request.FILES)  # Manejar archivos
#         if form.is_valid():
#             form.save()
#             return redirect('inmueble_list')
#     else:
#         form = InmuebleForm()
#     return render(request, 'registro_inmueble.html', {'form': form})






# @login_required
# def registro_inmueble(request):
#     if request.method == 'POST':
#         form = InmuebleForm(request.POST)
#         if form.is_valid():
#             inmueble = form.save(commit=False)
#             if not request.user.is_superuser:
#                 raise PermissionDenied("No tienes permiso para registrar inmuebles.")
#             inmueble.save()
#             return redirect('inmueble_list')  # Reemplaza con el nombre de la vista de la lista de inmuebles
#     else:
#         form = InmuebleForm()
#     return render(request, 'registro_inmueble.html', {'form': form})


@login_required
def registro_inmueble(request):
    if request.method == 'POST':
        form = InmuebleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inmueble_list')
    else:
        form = InmuebleForm()
    return render(request, 'registro_inmueble.html', {'form': form})



def inmueble_list(request):
    inmuebles = Inmueble.objects.all()
    return render(request, 'inmueble_list.html', {'inmuebles': inmuebles})


def inmueble_detail(request, inmueble_id):
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)
    return render(request, 'inmueble_detail.html', {'inmueble': inmueble})


def filtrar_inmuebles(request):
    form = FiltroInmuebleForm(request.GET or None)
    inmuebles = Inmueble.objects.all()

    if form.is_valid():
        zona = form.cleaned_data.get('zona')
        llegada = form.cleaned_data.get('llegada')
        salida = form.cleaned_data.get('salida')
        adultos = form.cleaned_data.get('adultos')
        niños = form.cleaned_data.get('niños')
        bebes = form.cleaned_data.get('bebes')
        mascotas = form.cleaned_data.get('mascotas')

        # Filtrar por zona
        if zona:
            if zona == 'norte':
                inmuebles = inmuebles.filter(region__in=['Arica y Parinacota', 'Tarapacá', 'Antofagasta', 'Atacama'])
            elif zona == 'centro':
                inmuebles = inmuebles.filter(region__in=['Coquimbo', 'Valparaíso', 'Región Metropolitana de Santiago', 'Región del Libertador Gral. Bernardo O’Higgins', 'Región del Maule'])
            elif zona == 'sur':
                inmuebles = inmuebles.filter(region__in=['Región de Ñuble', 'Región del Biobío', 'Región de la Araucanía', 'Región de Los Ríos', 'Región de Los Lagos'])
            elif zona == 'austral':
                inmuebles = inmuebles.filter(region__in=['Región Aisén del Gral. Carlos Ibáñez del Campo', 'Región de Magallanes y de la Antártica Chilena'])

        # Filtrar por fechas de disponibilidad
        if llegada:
            inmuebles = inmuebles.filter(fecha_disponible_desde__lte=llegada)
        if salida:
            inmuebles = inmuebles.filter(fecha_disponible_hasta__gte=salida)

        # Filtrar por capacidad
        if adultos is not None:
            inmuebles = inmuebles.filter(capacidad_adultos__gte=adultos)
        # Puedes agregar más lógica para niños, bebés y mascotas si es necesario

    return render(request, 'inmueble_list.html', {'form': form, 'inmuebles': inmuebles})








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