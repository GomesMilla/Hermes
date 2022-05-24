from os import name
from django.urls import path
from django.views.generic.base import View
from . import views


urlpatterns =[
    path('Login/', views.view_login, name='ViewLogin'),
    path('Create-Account/', views.view_create_account, name='createAccount'),
    
]