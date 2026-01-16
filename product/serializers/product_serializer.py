from rest_framework import serializers
from product.models import Product, Category
from .category_serializer import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        write_only=True,
        many=True
    )

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        category_data = validated_data.pop('category_id')
        product = Product.objects.create(**validated_data)
        for category in category_data:
            product.category.add(category)
        return product
