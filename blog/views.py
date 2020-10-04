from django.shortcuts import render
from .models import Blogpost

def index(request):
    data = Blogpost.objects.all()
    return render(request, 'blog/index.html', {"posts":data})

def blogPost(request):
    return render(request, 'blog/blogPost.html')