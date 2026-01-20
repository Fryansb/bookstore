import json
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework.authtoken.models import Token
from order.models import Order
from order.factories import OrderFactory, UserFactory
from product.factories import ProductFactory, CategoryFactory


class OrderViewSetTest(APITestCase):
    def setUp(self):
        # Criar usuário para autenticação
        self.auth_user = get_user_model().objects.create_user(
            username='authuser',
            password='testpass123'
        )
        self.token = Token.objects.create(user=self.auth_user)
        
        self.category = CategoryFactory(title="Electronics")
        self.product = ProductFactory(category=(self.category,))
        self.user = UserFactory()
        self.order = OrderFactory(user=self.user, product=(self.product,))

    def test_get_all_orders(self):
        """Test listing all orders"""
        token = Token.objects.get(user__username=self.auth_user.username)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        
        response = self.client.get('/bookstore/v1/order/')
        self.assertEqual(response.status_code, 200)
        
        order_data = json.loads(response.content)
        self.assertEqual(order_data[0]['product'][0]['title'], self.product.title)
        self.assertEqual(order_data[0]['product'][0]['price'], str(self.product.price))
        self.assertEqual(order_data[0]['product'][0]['active'], self.product.active)
        self.assertEqual(order_data[0]['product'][0]['category'][0]['title'], self.category.title)

    def test_create_order(self):
        """Test creating a new order"""
        token = Token.objects.get(user__username=self.auth_user.username)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        
        new_user = UserFactory()
        new_category = CategoryFactory(title="Books")
        new_product = ProductFactory(category=(new_category,))
        
        payload = {
            'product_id': [new_product.id],
            'user': new_user.id
        }
        
        response = self.client.post(
            '/bookstore/v1/order/',
            data=json.dumps(payload),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 201)
        created_order = Order.objects.get(id=response.data['id'])
        self.assertEqual(created_order.user, new_user)
        self.assertEqual(list(created_order.product.all()), [new_product])
