from django.shortcuts import render

def index(request):
    return render(request, 'polls/signin.html')
def signup(request):
    return render(request, 'polls/signup.html')
def blog(request):
    return render(request, 'polls/blog.html/')
