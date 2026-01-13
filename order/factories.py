import factory
from factory.django import DjangoModelFactory
from django.contrib.auth.models import User
from order.models import Order
from product.factories import ProductFactory


class UserFactory(DjangoModelFactory):
    username = factory.Faker('user_name')
    email = factory.Faker('email')

    class Meta:
        model = User


class OrderFactory(DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Order

    @factory.post_generation
    def product(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for prod in extracted:
                self.product.add(prod)
