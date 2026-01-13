from django.test import TestCase
from product.models import Category, Product
from product.factories import CategoryFactory, ProductFactory
from product.serializers import CategorySerializer, ProductSerializer


class CategorySerializerTest(TestCase):
    def setUp(self):
        self.category = CategoryFactory()

    def test_category_serializer_fields(self):
        """Test that CategorySerializer contains all expected fields"""
        serializer = CategorySerializer(instance=self.category)
        self.assertIn('id', serializer.data)
        self.assertIn('title', serializer.data)
        self.assertIn('slug', serializer.data)
        self.assertIn('description', serializer.data)
        self.assertIn('active', serializer.data)

    def test_category_serializer_data(self):
        """Test that CategorySerializer returns correct data"""
        serializer = CategorySerializer(instance=self.category)
        self.assertEqual(serializer.data['title'], self.category.title)
        self.assertEqual(serializer.data['slug'], self.category.slug)
        self.assertEqual(serializer.data['active'], self.category.active)


class ProductSerializerTest(TestCase):
    def setUp(self):
        self.category1 = CategoryFactory(title="Electronics")
        self.category2 = CategoryFactory(title="Books")
        self.product = ProductFactory(category=(self.category1, self.category2))

    def test_product_serializer_fields(self):
        """Test that ProductSerializer contains all expected fields"""
        serializer = ProductSerializer(instance=self.product)
        self.assertIn('id', serializer.data)
        self.assertIn('title', serializer.data)
        self.assertIn('description', serializer.data)
        self.assertIn('price', serializer.data)
        self.assertIn('active', serializer.data)
        self.assertIn('category', serializer.data)

    def test_product_serializer_with_categories(self):
        """Test that ProductSerializer includes nested CategorySerializer"""
        serializer = ProductSerializer(instance=self.product)
        self.assertEqual(len(serializer.data['category']), 2)
        self.assertIsInstance(serializer.data['category'], list)
        
    def test_product_serializer_price(self):
        """Test that product price is correctly serialized"""
        serializer = ProductSerializer(instance=self.product)
        self.assertEqual(str(serializer.data['price']), str(self.product.price))
