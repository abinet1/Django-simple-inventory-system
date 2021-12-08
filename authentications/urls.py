
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views as aute_views

urlpatterns = [
    path('login/', aute_views.LoginView.as_view(), name="login"),
    path("logout/", aute_views.LogoutView.as_view(), name="logout"),

]
