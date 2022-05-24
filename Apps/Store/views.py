from django.shortcuts import render
from django.views import generic
from Store.models import Product

class LadingPage(generic.ListView):
    model = Product
    context_object_name = 'list_queryset'
    template_name = 'Pages/LadingPage.html'
    #queryset = Product.objects.filter(title__icontains='war')[:5]