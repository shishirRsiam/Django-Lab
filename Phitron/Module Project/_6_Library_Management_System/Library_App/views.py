from django.shortcuts import redirect, render
from .models import User, Book, Categorie



def home(request):
    context = {
        'books' : Book.objects.all(),
        'categories' : Categorie.objects.all(),
        'is_additional_content' : 0,
    }
    return render(request, 'home.html', context)

def view_book(request, id):
    print("-> Book ID:", id)

    return render(request, 'view_book_info.html')


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