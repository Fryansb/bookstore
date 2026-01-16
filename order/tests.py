from django.test import TestCase
from decimal import Decimal
from order.models import Order
from order.factories import OrderFactory, UserFactory
from order.serializers import OrderSerializer
from product.factories import ProductFactory, CategoryFactory


class OrderSerializerTest(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.category = CategoryFactory()
        self.product1 = ProductFactory(price=Decimal('10.50'), category=(self.category,))
        self.product2 = ProductFactory(price=Decimal('20.00'), category=(self.category,))
        self.order = OrderFactory(user=self.user, product=(self.product1, self.product2))

    def test_order_serializer_fields(self):
        """Test that OrderSerializer contains all expected fields"""
        serializer = OrderSerializer(instance=self.order)
        self.assertIn('id', serializer.data)
        self.assertIn('user', serializer.data)
        self.assertIn('product', serializer.data)
        self.assertIn('total', serializer.data)

    def test_order_serializer_product_list(self):
        """Test that OrderSerializer includes product list"""
        serializer = OrderSerializer(instance=self.order)
        self.assertEqual(len(serializer.data['product']), 2)
        self.assertIsInstance(serializer.data['product'], list)

    def test_order_serializer_total_calculation(self):
        """Test that OrderSerializer calculates total correctly"""
        serializer = OrderSerializer(instance=self.order)
        expected_total = float(self.product1.price + self.product2.price)
        self.assertEqual(serializer.data['total'], expected_total)
        self.assertEqual(serializer.data['total'], 30.50)

    def test_order_serializer_empty_order(self):
        """Test OrderSerializer with order that has no products"""
        empty_order = OrderFactory(user=self.user)
        serializer = OrderSerializer(instance=empty_order)
        self.assertEqual(serializer.data['total'], 0.0)
        self.assertEqual(len(serializer.data['product']), 0)

    def test_order_serializer_user_field(self):
        """Test that OrderSerializer includes user ID"""
        serializer = OrderSerializer(instance=self.order)
        self.assertEqual(serializer.data['user'], self.user.id)
