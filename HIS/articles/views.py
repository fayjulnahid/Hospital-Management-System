from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article.html', {'articles': articles})


def article_detail(request, slug):
   # return HttpResponse(slug)
    article = Article.objects.get(sluge=slug)
    return render(request, 'articles/article_detail.html', {'article': article})

def appointment(request):
    return render(request,'articles/appointment.html')

@login_required(login_url="/accounts/login/")
def article_create(request):
    return render(request, 'articles/article_create.html')