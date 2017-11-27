from django.conf.urls import url
from django.contrib.auth.views import login
from . import views
from django.views.generic import ListView, DetailView
from polls.models import Posts

urlpatterns = [
    url(r'^signup/', views.signup, name='signup'),
    url(r'^signup_form/', views.signup_cr, name='signup'),
    url(r'^login/',login ,{'template_name':'polls/signin.html'}),
    url(r'^blog/', views.blog, name='blog'),

    #end here#
    
    url(r'^posts/', views.Postssss.as_view(), name='posts'),
    url(r'^(?P<pk>\d+)$', views.DPostssss.as_view(), name='dposts'),
    url(r'^followers/', views.followers, name='followers'),
    url(r'^messages/', views.followers, name='messages'),
    url(r'^tags/', views.followers, name='tags'),
    
    url(r'^create_post/', views.createpost, name='createpost'),
    url(r'^submit_post/', views.submit_post, name='createpost'),
]
