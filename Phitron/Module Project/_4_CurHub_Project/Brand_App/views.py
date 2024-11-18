from django.shortcuts import redirect, render


def add_brands(request):
    if not request.user.is_authenticated:
        return redirect('home')
    
    context = {
        'title': 'Add Brands',
    }
    return render(request, 'add_brands.html', context)