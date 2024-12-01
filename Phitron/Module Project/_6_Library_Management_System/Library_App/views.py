from .models import Book, Categorie, Borrow, Comment
from django.shortcuts import redirect, render
from django.contrib import messages
from decimal import Decimal

def home(request):
    context = {
        'books' : Book.objects.all(),
        'categories' : Categorie.objects.all(),
        'is_additional_content' : 0,
        'header_text' : 'Featured Books',
    }
    return render(request, 'home.html', context)

def view_books_filter_by_category(request, category_id):
    category = Categorie.objects.get(id=category_id)
    books = Book.objects.filter(categories=category)
    context = {
        'books' : books,
        'categories' : Categorie.objects.all(),
        'is_additional_content' : 0,
        'header_text' : f"'{category.name}' Featured Books",
    }
    return render(request, 'home.html', context)

def view_book(request, id):
    book = Book.objects.get(id=id)
    comments = book.comments.all().order_by('-id')

    can_review = False
    if request.user.is_authenticated:
        can_review = request.user.borrowed_books.filter(book=book)

    context = {
        'book': book,
        'comments' : comments,
        'can_review' : can_review,
    }

    if request.method == 'POST':
        text = request.POST.get('comment')
        
        comment = Comment.objects.create(
            user=request.user,
            book=book,
            comment_text=text
        )
        comment.save()

    return render(request, 'view_book_info.html', context)

def borrow_book(request, id):
    if not request.user.is_authenticated:
        return redirect('home')

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

    message = f"You have borrowed '{book.name}' for ${book.price}."
    messages.success(request, message)

    return redirect('profile')

def add_funds(request):
    if not request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        amount = request.POST.get('amount')
        request.user.account.balance += Decimal(amount)
        request.user.account.save()

        message = f'You have added ${amount} to your account.'
        messages.success(request, message)
        return redirect('profile')

    context = {
        'user': request.user,
    }
    return render(request, 'add_funds.html', context)
    # return redirect('home')

def return_book(request, borrow_id):
    if not request.user.is_authenticated:
        return redirect('home')

    borrow = Borrow.objects.get(id=borrow_id)
    if borrow.user == request.user:
        borrow.book.available_copies += 1
        borrow.book.save()

        borrow.user.account.balance += borrow.price
        borrow.user.account.save()

        borrow.is_returned = True
        borrow.after_balance = borrow.user.account.balance
        borrow.save()

        message = f"'{borrow.book.name}' has been returned successfully. Added ${borrow.price} to your account."
        messages.success(request, message)
    else:
        messages.error(request, 'You are not authorized to return this book.')

    return redirect('profile')

