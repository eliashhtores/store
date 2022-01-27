from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('applications.user.urls')),
    re_path('', include('applications.user.api_urls')),
    re_path('', include('applications.product.urls')),
    re_path('', include('applications.product.api_urls')),
    re_path('', include('applications.sale.api_urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
