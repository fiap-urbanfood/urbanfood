from django.db import models
import uuid
import produtos.models
from produtos.models import Produtos
from cliente.models import Cliente
from rest_framework.serializers import ModelSerializer


class Checkout(models.Model):
    status = models.BooleanField(default=False)
    fk_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.pk)


class Pedidos(models.Model):
    ACOMPANHAMENTO = [
        ("Recebido", "Recebido"),
        ("Em_preparação", "Em_preparação"),
        ("Pronto", "Pronto"),
        ("Finalizado", "Finalizado"),
    ]

    fk_produto = models.ForeignKey(Produtos, on_delete=models.CASCADE, null=True, blank=True)
    fk_checkout = models.ForeignKey(Checkout, on_delete=models.CASCADE, null=True, blank=True)


    numero_pedido = uuid.uuid4()
    status = models.CharField(
        max_length=100, null=True, blank=True, choices=ACOMPANHAMENTO
    )
    data = models.DateTimeField(auto_now_add=True)
