from django.shortcuts import render
from .models import Article, Hospital
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


def hospital_list(request):
    hospitals = Hospital.objects.all()
    return render(request, 'articles/hospital_list.html', {'hospitals': hospitals})

def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article.html', {'articles': articles})


def article_detail(request, slug):
   # return HttpResponse(slug)
    article = Article.objects.get(sluge=slug)
    return render(request, 'articles/article_detail.html', {'article': article})

def appointment(request):
    appointment.disease_name = request.POST.get('disease-name')
    appointment.name = request.POST.get('name')
    appointment.preferable_schedule = request.POST.get('preferable-schedule')
    appointment.adults = request.POST.get('adults')
    appointment.children = request.POST.get('children')
    appointment.cabin_category = request.POST.get('cabin-category')
    if request.method == "POST":


        #sending mail
        send_mail(
            'Mail Sent By ' + appointment.name,  # subject
            '\n Disease Information: ' + appointment.disease_name + '\n Name: ' + appointment.name + '\n Schedule: ' + appointment.preferable_schedule + ' \n Patient Information:\n ' +'Adults:' + appointment.adults +'\n Childern:' + appointment.children +'\n Cabin Information:' + appointment.cabin_category,
            # message
            appointment.name,  # from mail
            ['fayjulnahid2420@gmail.com'],  # to mail
        )

        return render(request, 'articles/appointment.html', {'name': appointment.name})
    else:
        return render(request,'articles/appointment.html')

#generating pdf filename
def appointment_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)


    disease_name = appointment.disease_name
    name = appointment.name
    schedule = appointment.preferable_schedule
    adults = appointment.adults
    childern = appointment.children
    cabin = appointment.cabin_category


    lines = [
        'Disease Name:' + disease_name,
        'Patient Name:' + name,
        'Schedule:' + schedule,
        'Adults:' + adults,
        'Children:' + childern,
        'Cabin:' + cabin,
    ]
    for line in lines:
        textob.textLine(line)
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='appointment.pdf')


@login_required(login_url="/accounts/login/")
def article_create(request):
    return render(request, 'articles/article_create.html')