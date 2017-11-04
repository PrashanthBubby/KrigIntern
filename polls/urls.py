from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^blog/', views.blog, name='blog'),
]