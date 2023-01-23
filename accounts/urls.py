from django.urls import path 

from . import views

app_name='start'

urlpatterns = [
    path('home', views.app,name="app"),
    path('', views.register,name='register'),
    path('login', views.loginPage,name='login'),
    path('logout', views.LogUserOut,name='logout'),
    path('fund-list', views.fundList, name='fund-list'),
    path('fund-create', views.fundCreate, name='fund-create'),
    path('fund-update/<int:id>', views.fundUpdate, name='fund-update'),
    path('fund-delete/<int:id>', views.fundDelete, name='fund-delete'),

   ]