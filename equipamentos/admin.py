from django.contrib import admin
from .models import Equipamento, Certificado, Caracteristica

# Register your models here.
class Equipamentos(admin.ModelAdmin):
    list_display = ['nome', 'fabricante', 'modelo', 'patrimonio', 'status']
    search_fields = ['nome']
    list_filter = ['patrimonio', 'status']
class Certificados(admin.ModelAdmin):
    list_display = ['equipamento', 'arquivo', 'data_calibracao', 'validade']
    search_fields = ['equipamento']
    list_filter = ['data_calibracao', 'validade']
class Caracteristicas(admin.ModelAdmin):
    list_display = ['equipamento', 'nome', 'valor']
    search_fields = ['equipamento']
    list_filter = ['nome', 'valor']
admin.site.register(Equipamento, Equipamentos)
admin.site.register(Certificado, Certificados)
admin.site.register(Caracteristica, Caracteristicas)