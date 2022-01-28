from rest_framework.routers import DefaultRouter
from . import api_views

router = DefaultRouter()
router.register(r'api/v1/product/colors',
                api_views.ColorViewSet, basename='colors')
urlpatterns = router.urls
