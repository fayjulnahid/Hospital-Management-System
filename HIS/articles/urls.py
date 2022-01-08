from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'articles'

urlpatterns = [
    url(r'^$', views.article_list, name="list"),
    url(r'^create/$',views.article_create,name="create"),
    url(r'^appointment/', views.appointment, name='appointment'),
    url(r'^appointment_pdf/', views.appointment_pdf, name='appointment_pdf'),
    url(r'^hospital_list/', views.hospital_list, name='hospital_list'),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),


]