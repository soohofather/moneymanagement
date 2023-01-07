from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm

# Create your views here.


def index(request):

    if request.user.is_authenticated:

        articles = Article.objects.filter(user=request.user).order_by("-date")

        total_incoming = 0
        total_spending = 0

        for article in articles:
            total_incoming += article.incoming
            total_spending += article.spending

        budget = total_incoming - total_spending

        context = {
            "articles": articles,
            "total_incoming": total_incoming,
            "total_spending": total_spending,
            "budget": budget,
        }

        return render(request, "articles/index.html", context)

    else:
        return render(request, "articles/index.html")


@login_required
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


@login_required
def detail(request, pk):

    article = Article.objects.get(pk=pk)

    context = {
        "article": article,
    }

    return render(request, "articles/detail.html", context)


@login_required
def delete(request, pk):

    article = Article.objects.get(pk=pk)

    article.delete()

    return redirect("articles:index")


@login_required
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
