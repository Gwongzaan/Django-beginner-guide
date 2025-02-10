from django.shortcuts import render
from .models import Blog 
# Create your views here.

def titles(request):
    blogs = Blog.objects.all()
    return render(request, template_name='blog/titles.html', context={'title': 'My blogs', "blogs": blogs})

def detail(request, id):
    post = Blog.objects.get(id=id)
    return render(request, template_name="blog/detail.html", context={"post": post})