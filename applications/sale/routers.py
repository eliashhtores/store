from rest_framework.routers import DefaultRouter
from . import api_views

router = DefaultRouter()
router.register(r'api/v1/sale', api_views.SaleViewSet, basename='sales')

urlpatterns = router.urls
