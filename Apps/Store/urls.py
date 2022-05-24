from os import name
from django.urls import path
from django.views.generic.base import View
from . import views


urlpatterns =[
    path('', views.LadingPage.as_view(), name='LadingPage'),
    
]