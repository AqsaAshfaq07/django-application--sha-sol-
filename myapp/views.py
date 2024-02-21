from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def products(request):
    products = Product.objects.all()
    products_list = list(products.values())
    context = {
        'products': products
    }
    return render(request, 'products.html', {'products': products})
