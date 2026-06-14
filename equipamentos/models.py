from django.db import models

# Create your models here.
class Equipamento(models.Model):
    class Status(models.TextChoices):
        ATIVO = 'ATIVO', 'Ativo'
        MANUTENCAO = 'MANUT', 'Em manutenção'
        INATIVO = 'INATIVO', 'Inativo'
    class Obra(models.TextChoices):
        OBRA_URUACU = 'OBRA_URUACU', 'OBRA BR 153 - URUAÇU - GO'
        OBRA_RIALMA = 'OBRA_RIALMA', 'OBRA BR 153 - RIALMA - GO'

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100, blank=True, null=True)
    serie = models.CharField(max_length=100)
    patrimonio = models.CharField(max_length=100)
    local = models.CharField()
    status = models.CharField(choices=Status.choices, default=Status.ATIVO)
    obra = models.CharField(choices=Obra.choices, default=Obra.OBRA_URUACU)
    obs = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return f"{self.nome}-{self.patrimonio}"

class Certificado(models.Model):
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    arquivo = models.FileField(upload_to="certificados/")
    data_calibracao = models.DateField()
    validade = models.DateField()

    def __str__(self):
        return self.equipamento.nome
    
class Caracteristica(models.Model):
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)

    def __str__(self):
        return self.equipamento.nome