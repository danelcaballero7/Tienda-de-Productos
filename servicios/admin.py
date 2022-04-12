from django.contrib import admin
from .models import Servicio


# Register your models here.
class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    class Meta:
        model = Servicio


admin.site.register(Servicio, ServicioAdmin)
