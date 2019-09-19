from django.shortcuts import render
from .models import Post
from django.utils import timezone

def main(request):
    posts = Post.objects.filter(published_date_lte=timezone.now()).order_by('published_date')
    return render(request,'blog/main.html',{'posts': posts})


def home(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/home.html',{'posts': posts})

def upload(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/upload.html',{'posts': form})

def feedback(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/feedback.html',{'posts': form})

    