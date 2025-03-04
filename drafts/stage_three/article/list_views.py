from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render

from .models import ArticleColumn, ArticlePost


def article_titles(request):
    article_title = ArticlePost.objects.all()
    paginator = Paginator(article_title, 2)
    page = request.GET.get("paga")

    try:
        current_page = paginator.page(page)
        articles = current_page.object_list

    except PageNotAnInteger:
        current_page = paginator.page(1)
        articles = current_page.object_list

    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
        articles = current_page.object_list

    return render(
        request,
        "article/list/article_titles.html",
        {"articles": articles, "page": current_page},
    )


def article_detail(request, id, slug):
    article = get_object_or_404(ArticlePost, id=id, slug=slug)
    return render(request, "article/list/article_content.html", {"article": article})
