from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.


def index(request):

    if request.user.is_authenticated:
        articles = Article.objects.filter(user=request.user)

        context = {
            "articles": articles,
        }

        return render(request, "articles/index.html", context)

    else:
        return render(request, "articles/index.html")


def create(request):

    if request.method == "POST":
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect("articles:index")
    else:
        article_form = ArticleForm()

    context = {
        "article_form": article_form,
    }

    return render(request, "articles/create.html", context)


def detail(request, pk):

    article = Article.objects.get(pk=pk)

    context = {
        "article": article,
    }

    return render(request, "articles/detail.html", context)


def delete(request, pk):

    article = Article.objects.get(pk=pk)

    article.delete()

    return redirect("articles:index")


def update(request, pk):

    if request.method == "POST":
        article = Article.objects.get(pk=pk)
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect("articles:detail", pk)
    else:
        review = Article.objects.get(pk=pk)
        article_form = ArticleForm(instance=review)

    context = {
        "article_form": article_form,
    }

    return render(request, "articles/update.html", context=context)
