from django.shortcuts import render
from .models import Product
from math import ceil

def index(request):
    data = Product.objects.all()
    count = len(data)
    slides = count//4 + ceil((count/4) - (count//4))
    print("count = "+str(count))
    print("slides = "+str(slides))
    allProducts = {
        "allProducts": data,
        "totalSlides": slides,
        "slideRange": range(2, slides+1)
    }
    return render(request, 'shop/index.html', allProducts)

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

