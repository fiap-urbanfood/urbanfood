from rest_framework import serializers
from pedidos.models import Checkout


class CheckoutSerializers(serializers.ModelSerializer):
    cliente = serializers.ReadOnlyField(source='fk_cliente.nome')
    class Meta:
        model = Checkout
        fields = "__all__"


