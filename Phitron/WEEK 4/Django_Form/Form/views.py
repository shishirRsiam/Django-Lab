from django.shortcuts import render

def home(request):
    print('---> from home')
    data = {}
    if request.POST:
        print('&*&'*20)
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')

        data = {
            'name' : name,
            'email' : email,
            'password' : password,
            'confirm_password' : confirm_password
        }

        # password = request.POST.get('password')
        print(request.POST)
        print(f'-> name: {name} \n-> email: {email}')
        print(f'-> password: {password} \n-> confirm_password: {confirm_password}')
        print('&*&'*20)
    return render(request, 'Form/home.html', {'data': data})

def homes(request):
    return render(request, 'Form/home.html')

def contact(request):
    return render(request, 'Form/contact.html')

def services(request):
    return render(request, 'Form/services.html')

def about(request):
    return render(request, 'Form/about.html')


def login(request):
    if request.POST:
        print('&*&'*20)
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')


        # password = request.POST.get('password')
        print(request.POST)
        print(f'-> name: {name} \n-> email: {email}')
        print(f'-> password: {password} \n-> confirm_password: {confirm_password}')
        print('&*&'*20)
    return render(request, 'Form/login.html')
