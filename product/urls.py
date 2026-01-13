from rest_framework.routers import SimpleRouter
from product.viewsets import ProductViewSet, CategoryViewSet

router = SimpleRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('product', ProductViewSet, basename='product')

urlpatterns = router.urls
