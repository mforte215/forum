from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Article
def index(request):
    latest_article_list = Article.objects.order_by("-published_date")
    context = {"latest_article_list": latest_article_list}
    return render(request, "app/index.html", context)

def articleDetail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    context = {"article": article}
    return render(request, "app/article.html", context)

def articleListView(request):
    try:
        articles = Article.objects.all()[:5]
        context = {"articles": articles}
        return render(request, "app/articles.html", context)
    except:
        raise Http404("No articles found!")