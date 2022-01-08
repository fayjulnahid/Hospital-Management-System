from django.apps import apps
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
#from HIS.articles.models import Article
nahid = apps.get_model('articles', 'Article')
nahid2 = apps.get_model('articles', 'Hospital')


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
        hospitals = nahid2.objects.filter(title__contains=searched)
        return render(request,'search_disease.html',{'searched': searched, 'diseases': diseases , 'hospitals': hospitals})

    else:
        return render(request, 'search_disease.html')

def contact_us(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # send an email
        send_mail(
            'Mail Sent By ' + name,  # subject
            '\n Senders Name: ' + name + '\n ' + 'Senders Email: ' + email + '\n Senders Subject: ' + subject + ' \n Message: ' + message,
            # message
            email,  # from mail
            ['fayjulnahid2420@gmail.com'],  # to mail
        )

        return render(request, 'contact_us.html', {'name': name})
    else:
        return render(request,'contact_us.html')

#def appointment(request):
    #return render(request,'appointment.html')
