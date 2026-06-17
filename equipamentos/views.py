from django.shortcuts import render, redirect
from .models import Equipamento, Caracteristica
# Create your views here.
def home(request):
    return redirect('equipamentos', obra='OBRA_URUACU')

def equipamentos(request, obra):
    statuses = request.GET.getlist('status')
    nome = request.GET.get('nome', '')
    local = request.GET.get('local', '')
    print('local:',local)
    equipamentos = Equipamento.objects.prefetch_related('certificado_set', 'caracteristica_set').filter(obra=obra)
    if statuses:
        equipamentos = equipamentos.filter(status__in=statuses)
    if nome:
        equipamentos = equipamentos.filter(nome__icontains=nome)
    if local:
        equipamentos = equipamentos.filter(local__icontains=local)
    return render(request, 'equipamentos.html', {'equipamentos': equipamentos, 'obra':obra, 'statuses':statuses, 'nome':nome, 'local': local})

def caracteristica(request, obra, id):
    equip = Equipamento.objects.get(id=id)
    caract = Caracteristica.objects.filter(equipamento=equip)
    return render(request, 'caracteristica.html', {'caracteristicas': caract, 'equipamento': equip, 'obra':obra})