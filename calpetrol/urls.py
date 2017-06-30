from django.conf.urls import url
from . import views

app_name = 'calpetrol'
urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^cal/$', views.calculate, name='cal'),
    url(r'^signup/$', views.signup, name='signup'),
]


 
