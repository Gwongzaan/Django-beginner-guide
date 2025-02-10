from django.shortcuts import get_object_or_404, render

from blog.models import Blog

# Create your views here.


def titles(request):
    blogs = Blog.objects.all()
    return render(request, template_name="blog/titles.html", context={"blogs": blogs})


def post(request, post_id):
    # post = Blog.objects.get(id=post_id)
    post = get_object_or_404(Blog, id=post_id)
    pub = post.published
    return render(request, "blog/content.html", {"post": post, "publish": pub})
