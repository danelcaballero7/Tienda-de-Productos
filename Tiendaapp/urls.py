from django.urls import path
from Tiendaapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('home/', views.home,name='Home'),
    path('tienda/', views.tienda, name='Tienda'),
    path('blog/', views.blog, name='Blog'),
    path('contacto/', views.contacto, name="Contacto"),
]
