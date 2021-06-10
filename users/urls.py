"""Users URLs"""
#Django
from django.contrib.auth.views import LogoutView
from django.db import router
from django.urls import path

#Views
from users import views

urlpatterns = [

    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login',
    ),

    path(
        route='logout/',
        view=views.LogoutView.as_view(),
        name='logout'
    ),

    path(
        route='signup/',
        view=views.SignupView.as_view(),
        name='signup',
    ),
    

]