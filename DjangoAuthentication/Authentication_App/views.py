from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def home(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        print('_+_+' * 15, "Authenticated User:", request.user)
        context = {
            'message': 'Welcome back, {}!'.format(request.user.username),
        }
        return render(request, 'home.html', context)

    print('_+_+' * 15, "Anonymous User")
    context = {
        'message': 'Please log in to access more features.',
    }
    return render(request, 'base.html', context) 


from .forms import SignUpForm
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()  # This saves the new user
            messages.success(request, 'Account created successfully!')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SignUpForm()
    
    return render(request, 'signup.html', {'form': form})


def signup_by_html(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password == confirm_password:
            # Create new user if it doesn’t exist
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                print(user)
                messages.success(request, 'Account created successfully!')
                return redirect('login')  # Redirect to the login page
            else:
                messages.error(request, 'Username already taken.')
        else:
            messages.error(request, 'Passwords do not match.')
    
    # Render the signup page
    return render(request, 'signup.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    context = {

    }

    if request.method == 'POST':
        # Retrieve form data
        user_username = request.POST.get('username')
        user_password = request.POST.get('password')
        
        # Debug print statements
        print("*" * 100, user_username, user_password)

        # Authenticate the user
        user = authenticate(username=user_username, password=user_password)
        print("*" * 100, user)

        # If authentication is successful
        if user is not None:
            login(request, user)  # Log the user in
            return redirect('home')
        else:
            context['message'] = "Invalid username or password!"

    # Render the login page for GET requests or if login fails
    return render(request, 'login.html', context)


@login_required
def logout_view(request):
    logout(request) 
    return redirect('home') 


from django.contrib.auth import update_session_auth_hash
def change_password(request):
    if not request.user.is_authenticated:
        return redirect('home')
    # is_authenticated
    context = {}

    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        # Ensure new and confirm password match
        if new_password != confirm_password:
            context['message'] = "New passwords do not match!"
            return render(request, 'change_password.html', context)

        # Verify current password
        # If you want change password without checking comment out this code...
        if not request.user.check_password(current_password):
            context['message'] = "Current password is incorrect!"
            return render(request, 'change_password.html', context)
        
        # Update the password
        request.user.set_password(new_password)
        request.user.save()

        # Keep the user logged in after changing password
        update_session_auth_hash(request, request.user)

        return redirect('home')  # Redirect to home or another page
    
    return render(request, 'change_password.html', context)

def edit_profile(request):
    if not request.user.is_authenticated:
        return redirect('home')
    context = {}

    if request.method == 'POST':
        print('&^'*30)
        email = request.POST.get('email')
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        print(first_name, last_name, email, username)

        request.user.email = email
        request.user.username = username
        request.user.first_name = first_name
        request.user.last_name = last_name
        request.user.save()
        context['message'] = "Profile updated successfully!"

    return render(request, 'edit_profile.html', context)
