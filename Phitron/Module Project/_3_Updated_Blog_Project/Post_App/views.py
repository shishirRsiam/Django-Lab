from django.shortcuts import redirect, render
from Categories_App.models import Categories
from .models import Post
from django.contrib.auth.models import User

def home(request):
    context = {
        'top_post' : get_most_viewed_post(),
        'title_text' : 'Posts',
        'categories' : Categories.objects.all(),
        'posts' : Post.objects.all(),
    }

    if request.user.is_authenticated:
        return render(request, 'authenticated_home.html', context)
    
    return render(request, 'home.html', context)

def get_most_viewed_post():
    post = Post.objects.order_by('-views')[:5]
    return post


def view_post_by_category(request, slug):
    top_post = get_most_viewed_post()
    category = Categories.objects.get(slug=slug)
    context = {
        'top_post' : top_post,
        'title_text' : f' {category.name} Categories Posts',
        'categories' : Categories.objects.all(),
        'posts' : Post.objects.filter(categories = category),
    }

    if request.user.is_authenticated:
        return render(request, 'authenticated_home.html', context)
    
    return redirect('home')


def add_post(request):
    if not request.user.is_authenticated:
        return redirect('login')

    context = {
        'Categories': Categories.objects.all(),
    }

    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        category_ids = request.POST.getlist('categories')  # getlist for ManyToMany field
        author = request.user  # Directly using the User object, not the ID

        # Ensure that the post with the same title doesn't exist
        if not Post.objects.filter(title=title).exists():
            post = Post(title=title, author=author, content=content)

            # Save content to a text file using the set_content method
            # post.set_content(content)

            # Add categories to the ManyToMany field after saving the post
            post.save()  # Save the Post object first
            post.categories.add(*category_ids)  # Unpack the category IDs list

        return redirect('viewpost', url=post.slug_url)

    return render(request, 'add_post.html', context)


from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
def view_post(request, url):
    try:
        post = get_object_or_404(Post, slug_url=url)
    except Http404:
        return redirect('home')
    
    post.views += 1
    post.save()
    context = {
        'post' : post,
    }
    return render(request, 'view_post.html', context)


def delete_post(request, slug_url):
    post = Post.objects.get(slug_url=slug_url)
    if not request.user.is_authenticated or post.author != request.user:
        return redirect('viewpost', url = post.slug_url)

    post.delete()
    return redirect('home')