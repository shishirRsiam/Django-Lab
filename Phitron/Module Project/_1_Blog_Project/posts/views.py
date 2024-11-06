from django.http import HttpResponse
from django.shortcuts import redirect, render
from posts.models import Post
from .forms import PostForm


def posts(request):
    posts = Post.objects.all().order_by('id')
    return render(request, 'posts/post_home.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    text = 'Add Post'
    btn_name = 'Submit'
    form = PostForm()
    return render(request, 'posts/post_add.html', {'form' : form, 'text': text, 'btn_name' : btn_name})

def delete_post(request, post_id):
    Post_Obj = Post.objects.get(id = post_id)
    Post_Obj.delete()
    return redirect('/')

def view_post(request, post_id):
    Post_Obj = Post.objects.get(id=post_id)
    Post_Obj.views += 1
    Post_Obj.save()
    return render(request, 'posts/post_view.html', {'post' : Post_Obj})

def edit_post(request, post_id):
    Post_Obj = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=Post_Obj)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    text = 'Edit Post'
    btn_name = 'Save'
    form = PostForm(instance=Post_Obj)
    return render(request, 'posts/post_add.html', {'form' : form, 'text': text, 'btn_name' : btn_name})
