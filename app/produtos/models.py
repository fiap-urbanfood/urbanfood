from django.db import models


class Produtos(models.Model):
    CATEGORIA = [
        ("Lanche", "Lanche"),
        ("Acompanhamento", "Acompanhamento"),
        ("Bebida", "Bebida"),
        ("Sobremesa", "Sobremesa"),
    ]

    nome = models.CharField(max_length=100, null=True, blank=True)
    categoria = models.CharField(
        max_length=100, null=True, blank=True, choices=CATEGORIA
    )
    preco_unitario = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.pk)
