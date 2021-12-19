from django.apps import apps
from django.http import HttpResponse
from django.shortcuts import render
#from HIS.articles.models import Article
nahid=apps.get_model('articles', 'Article')


def homepage(request):
    # return HttpResponse('homepage')
    return render(request,'homepage.html')
def about(request):
    # return HttpResponse('about')
    return render(request,'about.html')

def search_disease(request):
    if request.method == "POST":
        searched = request.POST['searched']

        diseases = nahid.objects.filter(title__contains=searched)
        return render(request,'search_disease.html',{'searched': searched, 'diseases':diseases})
    else:
        return render(request, 'search_disease.html')

def contact_us(request):
    return render(request,'contact_us.html')

#def appointment(request):
    #return render(request,'appointment.html')