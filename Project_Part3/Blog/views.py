from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Blog.models import NewPost, Comment
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

@login_required
def editPost(request, id):
  post = get_object_or_404(NewPost, id=id)
  if request.user == post.author or request.user.is_superuser:
    # Lógica de edición de post
    return render(request, 'AppFood/edit_post.html', {'post': post})
  else:
    messages.error(request, "No tienes permisos para editar este post")

    return redirect('AppFood/post_detalle.html', id=id)

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
    success_url = "/Blog/post-list"
    fields = ['titulo', 'body']

class PostUpdate(UpdateView):
    model = NewPost
    success_url = "/Blog/post-list"
    fields = ['titulo', 'body']

class PostDelete(DeleteView):
    model = NewPost
    success_url = "/Blog/post-list"

def comment(request, id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post_id=id
            new_comment.save()
            return redirect('comment_success')
    comments = Comment.objects.filter(post_id=id)
    post = NewPost.objects.get(id=id)
    form = CommentForm()
    context = {
        'form': form,
        'comments': comments,
        'post': post,
    }
    return render(request, 'AppFood/comment_form.html', context)


def comment_success(request):
    return render(request, 'AppFood/comment_success.html')
