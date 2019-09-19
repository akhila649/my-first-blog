from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect

def main(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    return render(request,'blog/main.html',{'posts': posts})


def home(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    return render(request,'blog/home.html',{'posts': posts})

def upload(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/upload.html',{'posts': form})

def feedback(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/feedback.html',{'posts': form})

def main(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('main',pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/main.html',{'form': form})   

def home(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('home',pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/home.html',{'form': form}) 
def upload(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('home',pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/home.html',{'form': form})
def feedback(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('home',pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/home.html',{'form': form})                


             

    