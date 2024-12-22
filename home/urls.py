from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from home.sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path("", views.index, name="home"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('delete-comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
