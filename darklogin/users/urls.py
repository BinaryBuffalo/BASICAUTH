from django.urls import include, path
from django.views.generic import TemplateView
from .views import *

app_name = "users"
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', registerPage, name='register'),
    path('login_view/', login_view, name="login_view"),
    path('logout/', Logout, name="Logout")
]