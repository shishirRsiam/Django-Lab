from django.shortcuts import redirect, render
from Categories_App.models import Categories
from .models import Post
from django.contrib.auth.models import User

def home(request):
    context = {
        'categories' : Categories.objects.all(),
        'posts' : Post.objects.all(),
    }
    print(context)

    if request.user.is_authenticated:
        return render(request, 'authenticated_home.html', context)
    
    return render(request, 'home.html', context)

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
            post.save()  # Save the Post object first

            # Save content to a text file using the set_content method
            # post.set_content(content)

            # Add categories to the ManyToMany field after saving the post
            post.categories.add(*category_ids)  # Unpack the category IDs list

        return redirect('home')

    return render(request, 'add_post.html', context)


def view_post(request, url):
    post = Post.objects.get(slug_url=url)
    post.views += 1
    post.save()
    context = {
        'post' : post,
    }

    return render(request, 'view_post.html', context)
