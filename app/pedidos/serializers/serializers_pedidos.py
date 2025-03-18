from rest_framework import serializers
from pedidos.models import Pedidos


class PedidosSerializers(serializers.ModelSerializer):
    produto = serializers.ReadOnlyField(source='fk_produto.nome')
    status_ckeckout = serializers.ReadOnlyField(source='fk_checkout.status')
    class Meta:
        model = Pedidos
        fields = "__all__"


class PedidosStatusSerializers(serializers.ModelSerializer):
    #produto = serializers.ReadOnlyField(source='fk_produto.nome')
    class Meta:
        model = Pedidos
        fields = ['status']