from django.shortcuts import render

from .models import Product


def index(request):
    return render(request, 'shop/index.html')

def aboutus(request):
    return render(request, 'shop/aboutus.html')

def contactus(request):
    return render(request, 'shop/contactus.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def productview(request):
    data = Product.objects.all()
    allProducts = {
        "allProducts": data
    }
    return render(request, 'shop/productview.html', allProducts)

def search(request):
    return render(request, 'shop/search.html')

def checkout(request):
    return render(request, 'shop/checkout.html')

