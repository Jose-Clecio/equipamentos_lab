from django.shortcuts import render
from .models import Equipamento, Caracteristica
# Create your views here.
def equipamentos(request):
    equipamentos = Equipamento.objects.prefetch_related('certificado_set')
    return render(request, 'equipamentos.html', {'equipamentos': equipamentos})

def caracteristica(request, id):
    equip = Equipamento.objects.get(id=id)
    caract = Caracteristica.objects.filter(equipamento=equip)
    return render(request, 'caracteristica.html', {'caracteristicas': caract, 'equipamento': equip})