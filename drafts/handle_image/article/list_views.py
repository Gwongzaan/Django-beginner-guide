import redis
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .forms import CommentForm
from .models import ArticleColumn, ArticlePost, Comment

r = redis.StrictRedis(
    host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB
)


def article_titles(request, username=None):
    if username:
        user = User.objects.get(username=username)
        article_title = ArticlePost.objects.filter(author=user)
        try:
            userinfo = user.userinfo
        except:
            userinfo = None
    else:
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

    if username:
        return render(
            request,
            "article/list/author_articles.html",
            {
                "articles": articles,
                "page": current_page,
                "userinfo": userinfo,
                "user": user,
            },
        )

    return render(
        request,
        "article/list/article_titles.html",
        {"articles": articles, "page": current_page},
    )


def article_detail(request, id, slug):
    article = get_object_or_404(ArticlePost, id=id, slug=slug)
    total_views = r.incr(f"article:{article.id}:views")
    r.zincrby("article_ranking", 1, article.id)
    article_ranking = r.zrange("article_ranking", 0, -1, desc=True)[:10]
    article_ranking_ids = [int(id) for id in article_ranking]
    most_viewed = list(ArticlePost.objects.filter(id__in=article_ranking_ids))
    most_viewed.sort(key=lambda x: article_ranking_ids.index(x.id))

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.save(0)

    else:
        comment_form = CommentForm()

    article_tags_ids = article.article_tag.values_list("id", list=True)
    similar_articles = ArticlePost.objects.filter(
        article_tag__in=article_tags_ids
    ).exclude(id=article.id)
    similar_articles = similar_articles.annotate(
        same_tags=Count("article_tag")
    ).order_by("-same_tags", "-created")[:4]

    return render(
        request,
        "article/list/article_content.html",
        {
            "article": article,
            "total_views": total_views,
            "most_viewed": most_viewed,
            "comment_form": comment_form,
            "similar_articles": similar_articles,
        },
    )


@csrf_exempt
@require_POST
@login_required()
def like_article(request):
    article_id = request.POST.get("id")
    action = request.POST.get("action")

    if article_id and action:
        try:
            article = ArticlePost.objects.get(id=article_id)
            if action == "like":
                article.users_like.add(request.user)
                return HttpResponse("1")
            else:
                article.users_like.remove(request.user)
                return HttpResponse("2")

        except:
            return HttpResponse("no")
