from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), 
    path('profiles/', include('profiles.urls')),
    path('products/', include('products.urls', namespace='products')),
    path('', include('home.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('checkout/', include('checkout.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)