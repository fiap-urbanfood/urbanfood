from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    cpf = models.CharField(max_length=100, null=True, blank=True)
    data_aniversario = models.DateField(null=True, blank=True)
    profissao = models.CharField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
