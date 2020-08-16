from django.shortcuts import render


def index(request):
    return render(request, 'shop/index.html')

def aboutus(request):
    return render(request, 'shop/aboutus.html')

def contactus(request):
    return render(request, 'shop/contactus.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def productview(request):
    return render(request, 'shop/productview.html')

def search(request):
    return render(request, 'shop/search.html')

def checkout(request):
    return render(request, 'shop/checkout.html')

