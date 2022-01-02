from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


#generating pdf file
def appointment_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    lines = [
        "This is Line 1"
        "This is Line 2"
        "This is Line 3"
    ]
    for line in lines:
        textob.textLine(line)
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='appointment.pdf')

def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article.html', {'articles': articles})


def article_detail(request, slug):
   # return HttpResponse(slug)
    article = Article.objects.get(sluge=slug)
    return render(request, 'articles/article_detail.html', {'article': article})

def appointment(request):
    if request.method == "POST":
        disease_name = request.POST['disease-name']
        preferable_doc = request.POST['preferable-doc']
        preferable_schedule = request.POST['preferable-schedule']
        adults = request.POST['adults']
        children = request.POST['children']
        cabin_category = request.POST['cabin-category']

        return render(request, 'articles/appointment.html', {'disease_name': disease_name})
    else:
        return render(request,'articles/appointment.html')

@login_required(login_url="/accounts/login/")
def article_create(request):
    return render(request, 'articles/article_create.html')