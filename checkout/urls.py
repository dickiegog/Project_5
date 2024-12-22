from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
    path('', views.checkout, name='checkout'), 
    path('success/', views.success, name='success'),
    path('save_profile_data/', views.save_profile_data, name='save_profile_data'),
    path("create-checkout-session/", views.create_checkout_session, name="create_checkout_session"),
]
