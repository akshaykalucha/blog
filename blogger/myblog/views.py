from django.shortcuts import render
from django.http import HttpResponse
from .models import Post 
# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'myblog/home.htm', context)

def about(request):
    return render(request, 'myblog/about.htm', {'title': 'About'})