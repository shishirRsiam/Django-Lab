from django.shortcuts import redirect, render
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login, logout

from . models import User

def signup_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    context = {}
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if User.objects.filter(username = username).exists():
            context['error_msg'] = 'Username already exists!'
            return render(request, 'signup.html', context)
        
        elif password != confirm_password:
            context['error_msg'] = "Passwords do not match!"
            return render(request, 'signup.html', context)
        
        else:
            NewUser = User.objects.create_user(
                first_name = first_name, last_name = last_name,
                username = username, email = email, password = password)
            NewUser.save()
            return redirect('login')

    return render(request, 'signup.html', context)

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    context = {}

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)
        if user:
            login(request, user)
            return redirect('home')
        context['error_msg'] = "Invalid username or password!"        

    return render(request, 'login.html', context)

def logout_page(request):
    if not request.user.is_authenticated:
        return redirect('home')
    
    logout(request)
    return redirect('home')

def profile_page(request):
    if not request.user.is_authenticated:
        return redirect('login')

    # Purchases = Purchase.objects.filter(user=request.user).order_by('-id')
    context = {
        # 'Purchases' : Purchases,
    }
    return render(request, 'profile.html', context)

def edit_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        request.user.username = request.POST['username']
        request.user.email = request.POST['email']
        request.user.first_name = request.POST['first_name']
        request.user.last_name = request.POST['last_name']
        request.user.save()
        return redirect('profile')

    context = {}
    return render(request, 'edit_profile.html', context)

def change_password(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    context = {}
    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        
        if not request.user.check_password(old_password):
            context['error_msg'] = 'Old password is incorrect!'

        elif new_password != confirm_password:
            context['error_msg'] = 'New password and confirm password do not match!'
        
        else:
            request.user.set_password(new_password)
            request.user.save()

            update_session_auth_hash(request, request.user)
            return redirect('profile')
    
    return render(request, 'change_password.html', context)
    
def help(request):
    return redirect('home')