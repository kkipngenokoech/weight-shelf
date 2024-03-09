from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ShelfViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'shelves', ShelfViewSet)

urlpatterns = router.urls