from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
# from .routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('cart.urls')),
    # path('', include('profiles.urls')),
    # path('', include('products.urls')),
    path('api/', include('djoser.urls')),
    re_path(r'auth/', include('djoser.urls.authtoken')),
    path('api/', include('products.urls')),
    path('api/', include('profiles.urls')),
    path('api/', include('order.urls')),
    # path('api/v1/auth/', include('rest_auth.urls')),
    # path('api/v1/auth/', include('allauth.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
