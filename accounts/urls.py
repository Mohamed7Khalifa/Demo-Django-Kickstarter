from django.urls import path 

from . import views

app_name='start'

urlpatterns = [
    path('home', views.app,name="app"),
    path('', views.register,name='register'),
    path('login', views.loginPage,name='login'),
    path('logout', views.LogUserOut,name='logout'),

   ]