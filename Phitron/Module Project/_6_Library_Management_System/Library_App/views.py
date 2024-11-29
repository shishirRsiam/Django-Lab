from django.shortcuts import redirect, render
from .models import User, Book, Categorie, Borrow

from decimal import Decimal

def home(request):
    context = {
        'books' : Book.objects.all(),
        'categories' : Categorie.objects.all(),
        'is_additional_content' : 0,
    }
    return render(request, 'home.html', context)

def view_book(request, id):
    print("-> Book ID:", id)
    categories = Categorie.objects.all()
    book = Book.objects.get(id=id)
    context = {
        'book': book,
        'categories': categories,
    }

    return render(request, 'view_book_info.html', context)


def view_books_filter_by_category(request, category_id):
    # brand = Brand.objects.get(id=brand_id)
    # cars = Car.objects.filter(brand=brand_id)
    context = {
        # 'header_text' : f"'{brand.name}' Featured Cars for Sale",
        # 'Brands' : Brand.objects.all(),
        # 'Cars' : cars,
        # 'projects' : [1, 2, 3],
    }
    # return render(request, 'home.html', context)
    return redirect('home')

def borrow_book(request, id):
    if not request.user.is_authenticated:
        return redirect('home')

    print('(-)'*20)
    book = Book.objects.get(id=id)
    book.available_copies -= 1
    book.save()
    
    request.user.account.balance -= book.price
    request.user.account.save()

    borrow = Borrow.objects.create(
        user=request.user, 
        book=book,
        after_balance=request.user.account.balance, 
        price=book.price) 
    borrow.save()

    print('(-)'*20)
    return redirect('profile')

def add_funds(request):
    if not request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        amount = request.POST.get('amount')
        request.user.account.balance += Decimal(amount)
        request.user.account.save()
        return redirect('profile')

    context = {
        'user': request.user,
    }
    return render(request, 'add_funds.html', context)
    # return redirect('home')