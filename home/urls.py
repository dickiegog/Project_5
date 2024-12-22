from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),  # Root URL handled by the index view
]
