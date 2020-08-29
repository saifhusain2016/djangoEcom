from django.shortcuts import render
from .models import Product, Contact
from math import ceil

def index(request):
    data = Product.objects.all()
    category = list(set([i.category for i in data]))
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
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        query = request.POST.get('query')
        contact = Contact(name=name, phone=phone, email=email, query=query)
        contact.save()
    return render(request, 'shop/contactUs.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def productview(request, myId):
    selected = Product.objects.filter(id=myId)
    return render(request, 'shop/products.html', { "selectedProduct":selected[0] })

def search(request):
    return render(request, 'shop/search.html')

def checkout(request):
    data = Product.objects.all()
    return render(request, 'shop/checkout.html', { "products": data })

def home(request):
    return render(request, '')

def main(request):
    return render(request, '')
