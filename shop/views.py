from django.shortcuts import render
from .models import Product
from math import ceil


def index(request):
    data = Product.objects.all()
    category = list(set([i.category for i in data]))
    print("----------------------------------------")
    print(category)
    productsByCategory = []
    for c in category:
        p = list(filter(lambda x:x.category == c, data))
        count = len(p)
        slides = count // 4 + ceil((count / 4) - (count // 4))
        productsByCategory.append([p, slides, range(2, slides+1)])
    params = { "allProducts": productsByCategory }
    return render(request, 'shop/index.html', params)

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
