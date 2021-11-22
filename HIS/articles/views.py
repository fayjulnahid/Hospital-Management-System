from django.shortcuts import render
from .models import Article
from django.http import HttpResponse


def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article.html', {'articles': articles})


def article_detail(request,slug):
   # return HttpResponse(slug)
    article = Article.objects.get(sluge=slug)
    return render(request, 'articles/article.html', {'article': article})