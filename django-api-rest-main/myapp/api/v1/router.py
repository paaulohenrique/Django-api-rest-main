from rest_framework.routers import DefaultRouter
from .viewsets import ClientViewSet, ProductViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'clientes', ClientViewSet, basename='client')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = router.urls

