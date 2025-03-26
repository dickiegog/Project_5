from django.urls import path
from . import views
from .views import index, delete_comment
from .views import redirect_authenticated_user
from allauth.account.views import SignupView, LoginView
from django.contrib.sitemaps.views import sitemap

urlpatterns = [
    path("", views.index, name="home"),
    path('newsletter-signup/', views.newsletter_signup, name='newsletter_signup'),
    path('delete-comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),

 # Override login and signup to redirect logged-in users
   path("accounts/login/", redirect_authenticated_user(LoginView), name="account_login"),
   path("accounts/signup/", redirect_authenticated_user(SignupView), name="account_signup"),
]