from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create your views here.
def title(request):
    posts = Post.objects.all()
    return render(request, template_name='blog/titles.html', context={'blogs': posts})

def posts(request, id):
    post = get_object_or_404(Post, id=id)
    publish = post.published_date
    return render(request, template_name='blog/posts.html', context={'article': post, 'publish': publish})

