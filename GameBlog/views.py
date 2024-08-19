from django.shortcuts import render
from .models import Post 
def tryview(request):
    return render(request, "signup.html")

def homeview(request):
    posts = Post.objects.all()
    return render(request, "home.html", {'posts': posts})

