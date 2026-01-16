import json
from rest_framework.test import APITestCase
from product.models import Category
from product.factories import CategoryFactory


class CategoryViewSetTest(APITestCase):
    def setUp(self):
        self.category = CategoryFactory(title="Books")

    def test_get_all_categories(self):
        """Test listing all categories"""
        url = '/bookstore/v1/product/category/'
        response = self.client.get(url)
        print(f"URL: {url}, Status: {response.status_code}, Content: {response.content}")
        self.assertEqual(response.status_code, 200)
        
        category_data = json.loads(response.content)
        self.assertEqual(category_data[0]['title'], self.category.title)
        self.assertEqual(category_data[0]['slug'], self.category.slug)
        self.assertEqual(category_data[0]['active'], self.category.active)

    def test_create_category(self):
        """Test creating a new category"""
        payload = {
            'title': 'Technology',
            'description': 'Tech products',
            'active': True
        }
        
        url = '/bookstore/v1/product/category/'
        response = self.client.post(
            url,
            data=json.dumps(payload),
            content_type='application/json'
        )
        
        print(f"URL: {url}, Status: {response.status_code}, Content: {response.content}")
        self.assertEqual(response.status_code, 201)
        created_category = Category.objects.get(title='Technology')
        self.assertEqual(created_category.title, 'Technology')
