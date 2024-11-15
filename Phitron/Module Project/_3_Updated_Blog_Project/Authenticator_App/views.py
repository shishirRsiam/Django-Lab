from django.shortcuts import redirect, render
from django.contrib.auth.models import User 

def signup_page(request):
    context = {}

    if request.method == 'POST':
        print("-> User Create,")
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        # Add your logic here to create a new user

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


from django.contrib.auth import authenticate, login
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


from django.contrib.auth import logout
def logout_page(request):
    if not request.user.is_authenticated:
        return redirect('home')
    
    logout(request)
    return redirect('home')


def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    context = {}
    return render(request, 'profile.html', context)
    