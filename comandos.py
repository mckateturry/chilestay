##Se va a trabajar con 2 terminales uno para la base de datos y el otro para Django

##ANTES DE COMENZAR##
##--1.1--HABILITAR POSTGRES (Abrir terminal "la crearemos sera powershell que se transformara en postgres")
#psql -U postgres
#Password: Admin1234
#Enter y debería aparecer: postgres=#

##--1--CREAR Y ACTIVAR EL ENTORNO--- (Esto en powershell ---> Aquí se trabaja el proyecto/ el entorno virtual)
#python -m venv vdemo
#vdemo\Scripts\activate

##--2--VER LAS DEPENDENCIA E INSTALA LO NECESARIO--- (Esto en powershell)
#pip list
#pip install django
#instalar driver de base de datos en nuestro entorno virtual
#pip install psycopg2           ---> #Esto es postgres   #Esto debe instalarse de forma correcta  
  
#pip install --upgrade pip      ---> #Esto es actualización #Siempre se hace en cada entorno
#pip list                       ---> #Esto muestra lo que acabamos instalar

##--3--CREAR PROYECTO E INGRESAR A LA CARPETA--- (Esto en powershell)
#django-admin startproject sistema_base   ---> #Creamos el proyecto
#cd sistema_base                          ---> #Accedemos al proyecto

##--4--REVISAMOS EXPLORER Y ENTRAMOS A SETTINGS.PY--- (Abrir ventana settings.py)
#Entramos a settings.py y vamos a la linea 76 donde está: DATABASE = {} y lo reemplazamos por:

#DATABASES = {
 #   "default": {
  #      "ENGINE": "django.db.backends.postgresql",
   #     "NAME": "sistema_base",
    #    "USER": "postgres",
     #   "PASSWORD": "Admin1234",
      #  "HOST": "127.0.0.1",
       # "PORT": "5432",
#    }
#}

##--5--CREAR LA BASE DE DATOS (Terminal postgres ---> Aquí se trabaja la base de datos)
#A continuación de postgres=# hay que agregar:
#create database sistema_base;       ---> #Debería decir: CREATE DATABASE postgres=#

##--6--CREAR APPS--- (Esto en powershell)
#python manage.py startapp testadl

##--7--VINCULAR APPS AL PROYECTO--- (Abrir ventana settings.py)
#En settings.py línea 33 en: INSTALLED_APPS = [] agregar:
#   'testadl',

##--8--CREAR SUPER USUARIO--- (Esto en powershell)
#python manage.py createsuperuser --->  #Aquí se crea email y password, siempre el mismo Katy para no olvidar!-.-
#Despues de crear super usuario siempre colocar:
#python manage.py makemigrations
#python manage.py migrate

##--9--CREAR TEMPLATES--- (En explorer)
#Crear carpeta templates en la app      ---> #En este caso sería dentro de testadl
#Crear los html, con estructura básica  ---> #Como: base.html, index.html ...
#Crear metodo que despliega el html
#Crear ruta que enlaza a views de la app

##--10--GENERAR LAS MIGRACIONES/ MODELO---
#Sí está todo OK, se puede generar las migraciones
#Crear el modelo en models.py (En explorer) abrir y colocar en línea 3:

#class Pelicula(models.Model):
#    titulo = models.CharField(max_length=50)
#    descripcion = models.TextField(default="") #siempre con parentesis

#Guardar y ejecutar (Esto en powershell)
#python manage.py makemigrations  ---> #Debe crear: Create model ... (en esté caso los ... = Pelicula)
#En explorer dentro de la apps, en la carpeta migrations se crea un archivo: _initial.py #Importante: No borrar.

#python manage.py migrate  ---> #migrate se lleva toda la info a la base de datos

##--11--REVISAR BASE DE DATOS--- (Terminal postgres)
#\c sistema_base   ---> #Entra, en este caso a sistema_base
#\d sistema_base       ---> #Muestra las tablas que tiene, procede a desplegarse una List of relations

##--12--GENERAR FUNCTION VIEWS--- (En explorer)
#Abrir url.py y copiar/pegar, debajo de los from:
#from testadl import views
#Y en urlpatterns = [] agregar:      ---> #Cuando se levanta el servidor (url.py), Aquí se inicia en la ruta principal va a ir al metodo
#path('', views.index, name='index') ---> #llamado index (está en views.py) y va retornar el mensaje de la línea 95.

##--13--Ir a VIEWS.PY--- (En explorer)
#Agregar en url.py, HttpResponse. Debe quedar así:  <----- #CREO que me equivoque es views.py no url.py#

#from django.shortcuts import render,HttpResponse

#Y en: # Create your views here. agregar:

#def index(request):
#   return HttpResponse("Ejecucion correcta")

#o está opcion que es más completa:

#def index(request):
    #select * from peliculas;
#    peliculas = Pelicula.objects.all()
#    print(peliculas)
    
    #select * from peliculas WHERE titulo='Titanic';
#    pelicula_titanic = Pelicula.objects.filter(titulo = 'Titanic')
#    print (pelicula_titanic)
    
#    return HttpResponse("Ejecucion correcta")



##--14--AHORA A PROBAR! EJECUTAR--- (Esto en powershell)
#python manage.py runserver

##--15--CREAR MODELO AL ADMIN.PY--- (En explorer)
#En admin.py hay que primero hacer la importación:
#from .models import Pelicula             ---> #Significa: Desde los modelos importame Pelicula
#Luego en # Register your models here. agregar:
#admin.site.register(Pelicula)

##--16--DJANGO ADMINISTRATION--- (En browser)
#Debe aparecer "agregar pelicula" (en este caso)

#QUEDE EN 1:28:16 aprox, creo que debo retroceder un poco



#Aquí se puede trabajar en la terminal

#python manage.py shell ---> Dentro de la shell

#>>> from testadl.models import Persona
#>>> p1 = Persona(nombre='John', apellido='Doe', correo='jdoe@mail.com')
#crea o actualiza:
#>>> p1.save()
#>>> p2 = Persona(nombre='Chuck', apellido='Norris', correo='chuck@mail.com')
#>>> p2.save()




#ORM = ES UN MEDIADOR ENTRE LOS OBJETOS Y LA BASE DE DATOS genera una capa de abstracción Aquí no hay que hacer ninguna Query. Aquí va a preguntar
#a traves de un objeto



#python manage.py runserver 0.0.0.0:8000
#http://192.168.0.17:8000


#conocer todas las migraciones y saber cuales se han ejecutado en la base de datos

#________________________________________________________

#mostrar en consola
#python manage.py dumpdata --indent 2

#exportar a un archivo
#python manage.py