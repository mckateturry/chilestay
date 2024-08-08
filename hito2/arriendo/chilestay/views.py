from django.shortcuts import render
#from chilestay.views import index


# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
#from .models import Flan #Cafe, ContactForm
#from .forms import ContactoFormForm
#from django.contrib.auth.decorators import login_required
def index(request):
    # lógica para la vista
    return render(request, 'index.html')
