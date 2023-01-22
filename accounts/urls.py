from django.urls import path 

from . import views

app_name='start'

urlpatterns = [
    path('', views.app,name='app'),
    path('register.html', views.register,name='register'),
    path('login.html', views.loginPage,name='login'),

   ]