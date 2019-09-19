from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render,get_object_or_404

def main(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    return render(request,'blog/main.html',{'posts': posts})


def home(request):
    posts = get_object_or_404(Post, pk=pk)
    return render(request,'blog/home.html',{'posts': posts})

def upload(request):
    posts = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/upload.html',{'posts': posts})

def feedback(request):
    posts = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/feedback.html',{'posts': posts})

    