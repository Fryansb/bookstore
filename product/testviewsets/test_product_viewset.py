import json
from decimal import Decimal
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework.authtoken.models import Token
from product.models import Product
from product.factories import ProductFactory, CategoryFactory


class ProductViewSetTest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.token = Token.objects.create(user=self.user)
        
        self.category = CategoryFactory(title="Electronics")
        self.product = ProductFactory(
            title="Laptop",
            price=Decimal('1500.00'),
            category=(self.category,)
        )

    def test_get_all_products(self):
        """Test listing all products"""
        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        
        response = self.client.get('/bookstore/v1/product/product/')
        self.assertEqual(response.status_code, 200)
        
        product_data = json.loads(response.content)
        self.assertEqual(product_data[0]['title'], self.product.title)
        self.assertEqual(product_data[0]['price'], str(self.product.price))
        self.assertEqual(product_data[0]['active'], self.product.active)
        self.assertEqual(len(product_data[0]['category']), 1)
        self.assertEqual(product_data[0]['category'][0]['title'], self.category.title)

    def test_create_product(self):
        """Test creating a new product"""
        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        
        new_category = CategoryFactory(title="Books")
        
        payload = {
            'title': 'Notebook',
            'description': 'A good notebook',
            'price': '800.00',
            'active': True,
            'category_id': [new_category.id]
        }
        
        response = self.client.post(
            '/bookstore/v1/product/product/',
            data=json.dumps(payload),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 201)
        created_product = Product.objects.get(title='Notebook')
        self.assertEqual(created_product.title, 'Notebook')
        self.assertEqual(str(created_product.price), '800.00')
