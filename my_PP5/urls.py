from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from . import views
from django.conf import settings
from django.conf.urls.static import static
from products.models import Product

info_dict = {
    'queryset': Product.objects.all(), 
    'date_field': 'id',
}

# Define the sitemap dictionary
sitemaps = {
    "products": GenericSitemap({
        "queryset": Product.objects.all(),
        "date_field": "updated_at",  # Make sure this field exists in Product
    }),
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), 
    path('profiles/', include('profiles.urls')),
    path('products/', include('products.urls', namespace='products')),
    path('', include('home.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('checkout/', include('checkout.urls')),
     path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)