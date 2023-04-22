from django.shortcuts import render, redirect
from Blog.models import NewPost
from Blog.forms import PostForm

def insertPost(request):
    posts = NewPost.objects.filter(state=True)

    form = PostForm()
    if request.method =="POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect ('/')
    context = {'form': form, 'posts': posts}
    return render (request, 'AppFood/inicio.html', context)

def post(request, pk):
    post = NewPost.objects.get(id=pk)
    context = {'post': post}
    return render(request, 'AppFood/post.html', context)

def editPost (request, pk):
    post = NewPost.objects.get(id=pk)
    form = PostForm(isinstance= post)
    if request.method =="POST":
        form = PostForm(request.POST, request.FILES, isinstance= post)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form': form}
    return render(request, 'AppFood/inicio.html', context)





