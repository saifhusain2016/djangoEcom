from django.shortcuts import render
from .models import Blogpost

def index(request):
    data = Blogpost.objects.all()
    return render(request, 'blog/index.html', {"posts":data})

def blogPost(request, id):
    blogpost = Blogpost.objects.filter(post_id=id)[0]
    prev = ""
    next = ""
    x = Blogpost.objects.filter(post_id=id-1)
    if x.exists():
        prev=x[0];
    x = Blogpost.objects.filter(post_id=id+1)
    if x.exists():
        next = x[0];
    return render(request, 'blog/blogpost.html', {'blogData':blogpost, 'prev':prev, 'next':next})