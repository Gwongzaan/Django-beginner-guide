from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .forms import ArticleColumnForm, ArticlePostForm, ArticleTagForm
from .models import ArticleColumn, ArticlePost, ArticlTag


@login_required()
@csrf_exempt
def article_column(request):
    if request.method == "GET":
        columns = ArticleColumn.objects.filter(user=request.user)
        column_form = ArticleColumnForm()
        return render(
            request,
            "article/column/article_column.html",
            {"columns": columns, "column_form": column_form},
        )
    if request.method == "POST":
        column_name = request.POST["column"]
        print(column_name)
        columns = ArticleColumn.objects.filter(
            user_id=request.user.id, column=column_name
        )
        if columns:
            return HttpResponse("2")
        else:
            ArticleColumn.objects.create(user=request.user, column=column_name)
            return HttpResponse("1")


@login_required()
@require_POST
@csrf_exempt
def edit_article_column(request):
    column_name = request.POST["column_name"]
    column_id = request.POST["column_id"]
    try:
        line = ArticleColumn.objects.get(id=column_id)
        line.column = column_name
        return HttpResponse("1")
    except:
        return HttpResponse("0")


@login_required()
@require_POST
@csrf_exempt
def del_article_column(request):
    column_id = request.POST["column_id"]
    try:
        line = ArticleColumn.objects.get(id=column_id)
        line.delete()
        return HttpResponse("1")

    except:
        return HttpResponse("2")


@login_required()
@csrf_exempt
def article_post(request):
    if request.method == "POST":
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            cd = article_post_form.cleaned_data
            try:
                new_article = article_post_form.save(commit=False)
                new_article.author = request.user
                new_article.column = request.user.article_column.get(
                    id=request.POST["column_id"]
                )
                new_article.save()
                return HttpResponse("1")

            except Exception as e:
                return HttpResponse("2")

        else:
            return HttpResponse("3")

    else:
        article_post_form = ArticlePostForm()
        article_columns = request.user.article_column.all()
        return render(
            request,
            "article/column/article_post.html",
            {
                "article_post_form": article_post_form,
                "article_columns": article_columns,
            },
        )


@login_required()
def article_list(request):
    articles = ArticlePost.objects.filter(author=request.user)
    paginator = Paginator(articles, 2)
    page = request.GET.get("page")
    try:
        current_page = paginator.page(page)
        articles = current_page.object_list

    except PageNotAnInteger:
        current_page = paginator.page(1)
        articles = current_page.object_list
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
        articles = current_page.object_list
    except Exception:
        pass

    return render(
        request,
        "article/column/article_list.html",
        {"articles": articles, "page": current_page},
    )


@login_required()
def article_detail(request, id, slug):
    article = get_object_or_404(ArticlePost, id=id, slug=slug)
    return render(request, "article/column/article_detail.html", {"article": article})


@login_required()
@require_POST
@csrf_exempt
def del_article(request):
    article_id = request.POST["article_id"]
    try:
        article = ArticlePost.objects.get(id=article_id)
        article.delete()
        return HttpResponse("1")
    except:
        return HttpResponse("2")


@login_required()
@csrf_exempt
def edit_article(request, article_id):
    if request.method == "POST":
        article_columns = request.user.article_column.all()
        article = ArticlePost.objects.get(id=article_id)
        this_article_form = ArticlePostForm(initial={"title": article.title})
        this_article_column = article.column

        return render(
            request,
            "article/column/edit_article.html",
            {
                "article": article,
                "article_column": article_column,
                "this_article_form": this_article_form,
                "this_article_column": this_article_column,
            },
        )
    else:
        article = ArticlePost.objects.get(id=article_id)
        try:
            article.column = request.user.article_column.get(
                id=request.POST["column_id"]
            )
            article.title = request.POST["title"]
            article.body = request.POST["body"]
            article.save()
            return HttpResponse("1")

        except:
            return HttpResponse("2")


@login_required()
@csrf_exempt
def article_tag(request):
    if request.method == "GET":
        article_tags = ArticlTag.objects.filter(author=request.user)

        article_tag_form = ArticleTagForm()
        return render(
            request,
            "article/tag/tag_list.html",
            {"article_tags": article_tags, "article_tag_form": article_tag_form},
        )

    if request.method == "POST":
        tag_post_form = ArticleTagForm(request.POST)
        if tag_post_form.is_valid():
            try:
                new_tag = tag_post_form.save(commit=False)
                new_tag.author = request.user
                new_tag.save()
                return HttpResponse("1")
            except:
                return HttpResponse("data cannot be saved")
        else:
            return HttpResponse("form not valid")


@login_required()
@require_POST
@csrf_exempt
def del_article_tag(request):
    tag_id = request.POST["tag_id"]
    try:
        tag = ArticlTag.objects.get(id=tag_id)
        tag.delete()
        return HttpResponse("1")
    except:
        return HttpResponse("2")
