from django.shortcuts import redirect, render




def home(request):
    context = {
        'books' : [1, 2, 3, 4, 5],
        'categories' : [1, 2, 3, 4, 5, 6, 7],
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