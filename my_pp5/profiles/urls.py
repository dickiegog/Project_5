from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('edit/', views.edit_profile, name='edit_profile'),
    path('save_profile_data/', views.save_profile_data, name='save_profile_data'),
]
