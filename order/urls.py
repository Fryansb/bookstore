from rest_framework.routers import SimpleRouter
from order.viewsets import OrderViewSet

router = SimpleRouter()
router.register('', OrderViewSet, basename='order')

urlpatterns = router.urls
