from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('edit/', views.edit_profile, name='edit_profile'),
    path('save/', views.save_profile, name='save_profile'),
]
