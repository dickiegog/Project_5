from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap

urlpatterns = [
    path("", views.index, name="home"),
    path('delete-comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
