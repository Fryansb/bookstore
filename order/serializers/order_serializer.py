from rest_framework import serializers
from order.models import Order
from product.models import Product
from product.serializers import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        write_only=True,
        many=True
    )
    total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'user', 'product', 'product_id', 'total']
        extra_kwargs = {
            'product': {'required': False}
        }

    def get_total(self, instance):
        """Calculate the total price of all products in the order"""
        total = sum([product.price for product in instance.product.all()])
        return float(total)

    def create(self, validated_data):
        product_data = validated_data.pop('product_id')
        user_data = validated_data.pop('user')
        order = Order.objects.create(user=user_data, **validated_data)
        for product in product_data:
            order.product.add(product)
        return order
