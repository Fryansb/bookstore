import factory
from factory.django import DjangoModelFactory
from product.models import Category, Product


class CategoryFactory(DjangoModelFactory):
    title = factory.Faker('word')
    slug = factory.Faker('slug')
    description = factory.Faker('text')
    active = True

    class Meta:
        model = Category


class ProductFactory(DjangoModelFactory):
    title = factory.Faker('word')
    description = factory.Faker('text')
    price = factory.Faker('pydecimal', left_digits=5, right_digits=2, positive=True)
    active = True

    class Meta:
        model = Product

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for cat in extracted:
                self.category.add(cat)
