from django.shortcuts import redirect, render
from .models import Brand, Car, Comment, Purchase


def home(request):
    context = {
        'header_text' : 'Featured Cars for Sale',
        'Brands' : Brand.objects.all(),
        'Cars' : Car.objects.all(),
        'projects' : [1, 2, 3],
    }
    return render(request, 'home.html', context)


def view_cars_filter_by_brand(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    cars = Car.objects.filter(brand=brand_id)
    context = {
        'header_text' : f"'{brand.name}' Featured Cars for Sale",
        'Brands' : Brand.objects.all(),
        'Cars' : cars,
        'projects' : [1, 2, 3],
    }
    return render(request, 'home.html', context)

def buy_car(request, id):
    car = Car.objects.get(id=id)
    if car:
        car.quantity -= 1
        car.save()
        purchase = Purchase(car=car, user=request.user)
        purchase.save()
        return redirect('profile')

    context = {
        'Car' : car,
    }
    return redirect('view_info', car.id)

def view_info(request, id):
    car = Car.objects.get(id=id)
    context = {
        'Car' : car,
    }
    if request.method == 'POST':
        comment = Comment.objects.create(
            name=request.POST['name'],
            comment_text=request.POST['comment'],
            post=car)
        comment.save()

    return render(request, 'view_info.html', context)