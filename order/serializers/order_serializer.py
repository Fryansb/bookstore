from rest_framework import serializers
from order.models import Order
from product.serializers import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'user', 'product', 'total']

    def get_total(self, instance):
        """Calculate the total price of all products in the order"""
        total = sum([product.price for product in instance.product.all()])
        return float(total)
