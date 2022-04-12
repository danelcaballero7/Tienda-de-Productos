from django.shortcuts import render,HttpResponse


# Create your views here.
def home(request):
    return render(request, "Tiendaapp/home.html")

def tienda(request):
    return render(request, "Tiendaapp/tienda.html")

def blog(request):
    return render(request, "Tiendaapp/blog.html")

def contacto(request):
    return render(request, "Tiendaapp/contacto.html")
