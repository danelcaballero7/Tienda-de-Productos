from django.shortcuts import render,HttpResponse
from servicios.models import Servicio

# Create your views here.
def home(request):
    return render(request, "Tiendaapp/home.html")

def servicios(request):
    servicios= Servicio.objects.all()


    return render(request, "Tiendaapp/servicios.html", {'servicios':servicios})

def tienda(request):
    return render(request, "Tiendaapp/tienda.html")

def blog(request):
    return render(request, "Tiendaapp/blog.html")

def contacto(request):
    return render(request, "Tiendaapp/contacto.html")
