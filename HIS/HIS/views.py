from django.http import HttpResponse
from django.shortcuts import render
import HIS


def homepage(request):
    # return HttpResponse('homepage')
    return render(request,'homepage.html')
def about(request):
    # return HttpResponse('about')
    return render(request,'about.html')

def search_disease(request):
    if request.method == "POST":
        searched = request.POST['searched']

        #disease = HIS.articles.models.Article.objects.filter(title__contains=searched)
        return render(request,'search_disease.html',{'searched': searched})
    else:
        return render(request, 'search_disease.html')