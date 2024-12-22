from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_catalog, name='product_catalog'),
    path('add/', views.add_product, name='add_product'),
    path('update/<int:product_id>/', views.update_product, name='update_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]
