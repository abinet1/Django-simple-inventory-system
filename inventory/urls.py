
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views as inventory_views

urlpatterns = [
    path('', inventory_views.Home.as_view(), name="Home"),
]