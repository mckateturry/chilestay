"""
URL configuration for arriendo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from chilestay.views import index #hoy_view
from chilestay import views
from django.contrib.auth import views as auth_views
from chilestay.views import RegisterInmuebleView


"""urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),  # Usa la vista importada aquí
    path('inmueble/', views.inmueble_list, name='inmueble_list'),
]"""


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', index, name='index'),
    path('hoy/', views.hoy, name='hoy'),
    path('calendario/', views.calendario, name='calendario'), 
    path('reservaciones/', views.reservaciones, name='reservaciones'),
    path('modoanfitrion/', views.modoanfitrion, name='modoanfitrion'),
    path('register/', views.register, name='register'),
    #path('login/', views.login, name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('hosting/', views.hosting, name='hosting'),
    path('estadias/', views.estadias, name='estadias'),
    path('anuncios/', views.anuncios, name='anuncios'),
    
    #path('explorar/', views.explorar_propiedades, name='explorar_propiedades'),
    #path('registerinmuebles/', views.registerinmuebles, name='registerinmuebles'),
    path('filtrar-comunas/', views.filtrar_comunas, name='filtrar_comunas'), #corregido
    path('registerinmuebles/', RegisterInmuebleView.as_view(), name='registerinmuebles'),
    #path('', views.index, name='index'),
    #path('', include('arriendo.urls')),
]
