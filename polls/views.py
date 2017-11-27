from django.shortcuts import render , redirect
from django.shortcuts import HttpResponse
from polls.models import UserProfile
from polls.models import Posts
import datetime
from .forms import Posts_Details, User_Signup
from django.views import generic
from django.contrib.auth.models import User


def signup(request):
    return render(request, 'polls/signup.html')

def signup_cr(request):
    if request.method=='POST':
        form=User_Signup(request.POST)
    if form.is_valid():
        user_nme=form.cleaned_data['username']
        pswrd=form.cleaned_data['password']
        user = User.objects.create_user(user_nme,user_nme,pswrd)
        return redirect('blog')
    else: return HttpResponse('enter correct format')
    

#def blog(request):
#   return render(request,'polls/blog.html')


    
def submit_post(request):
    if request.method=='POST':
        form=Posts_Details(request.POST)
    if form.is_valid():
        post_title=form.cleaned_data['title']
        post_matter=form.cleaned_data['post']
        t=datetime.datetime.now()
        data=Posts(username=request.user,title=post_title,post=post_matter,date=t)
        data.save()
        return redirect('posts')
    else: return HttpResponse('some thing went wrong')

def blog(request):
    return render(request,'polls/blog.html')

def createpost(request):
    return render(request,'polls/post_entry.html')

#def submit_post(request):
 #   return render(request,'polls/posts_lists.html') 

def followers(request):
    return render(request, 'polls/signin_error.html')


class Postssss(generic.ListView):
    template_name='polls/posts_lists.html'
    def get_queryset(self):
        return Posts.objects.all().order_by('-date')
class DPostssss(generic.DetailView):
    model=Posts
    template_name='polls/detail_post.html'

