from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from . import views
from django.conf import settings
from django.conf.urls.static import static
from products.models import Product
from .views import sitemap_view
from django.views.generic import TemplateView

path('sitemap.xml', TemplateView.as_view(
    template_name='sitemap.xml',
    content_type='application/xml'
)),


info_dict = {
    'queryset': Product.objects.all(), 
    'date_field': 'id',
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), 
    path('profiles/', include('profiles.urls')),
    path('products/', include('products.urls', namespace='products')),
    path('', include('home.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('checkout/', include('checkout.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps_config}, name='sitemap'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)