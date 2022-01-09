
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r"^accounts/", include('accounts.urls')),
    url(r'^articles/', include('articles.urls')),
    url(r'^ /$', views.about),
    url(r'^$', views.homepage, name='homepage'),
    url(r'^search_disease/', views.search_disease, name='search_disease'),
    url(r'^contact_us/', views.contact_us, name='contact_us'),
    #url(r'^appointment/', views.appointment, name='appointment')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)