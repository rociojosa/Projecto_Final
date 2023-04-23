from django.shortcuts import render, redirect, get_object_or_404
from Blog.models import NewPost
from Blog.forms import PostForm, CommentForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

def insertPost(request):
    posts= NewPost.objects.all()

    if request.method =="GET":
        form = PostForm()
    else:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect ('/AppFood/')
    context = {'form': form, 'posts': posts}
    return render (request, 'AppFood/post.html', context)

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
        return redirect('Post')
    context = {'form': form}
    return render(request, 'AppFood/post.html', context)

def post_list(request):
    posts = NewPost.objects.all()
    context = {'posts':posts}
    return render(request, 'AppFood/post_list.html',context)
    
class PostDetalle(DetailView):
    model = NewPost
    template_name = "AppFood/post_detalle.html"

def detalle_vista(request, id):
    post = get_object_or_404(NewPost, id=id)
    context = {'post': post}
    return render(request, 'AppFood/post_detalle.html', context)

class PostCreacion(CreateView):
    model = NewPost
    sucess_url = "/AppFood/post/list"
    fields = ['titulo', 'body']

class PostUpdate(UpdateView):
    model = NewPost
    sucess_url = "/AppFood/post/list"
    fields = ['titulo', 'body']

class PostDelete(DeleteView):
    model = NewPost
    sucess_url = "/AppFood/post/list"

def comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AppFood/comment_success.html')
    else:
        form = CommentForm()
    return render(request, 'AppFood/comment_form.html', {'form': form})

def comment_success(request):
    return render(request, 'AppFood/comment_success.html')
