from django.contrib import admin

# Register your models here.
from administrativo.models import Edificio, Departamento

class EdificioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'ciudad', 'tipo')
    search_fields = ('nombre', 'direccion', 'ciudad')

admin.site.register(Edificio, EdificioAdmin)

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nombPropietario', 'costoDept', 'cuartos', 'edificio')
    raw_id_fields = ('edificio',)

admin.site.register(Departamento, DepartamentoAdmin)