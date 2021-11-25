from django.conf.urls import url
from.import views
from django.contrib.auth.views import LogoutView
from django.urls import include, path
from django.conf import settings


app_name = 'accounts'

urlpatterns = [
    url(r"^signup/$", views.signup_view, name="signup"),
    url(r'^login/$', views.login_view, name="login"),
    #url(r'^logout/$',views.logout_view,name="logout"),
    path('^logout/$', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
]