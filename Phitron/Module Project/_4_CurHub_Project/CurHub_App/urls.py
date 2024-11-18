from django.urls import include, path

from . import views as CurHub_App_Views


urlpatterns = [
    path('', CurHub_App_Views.home, name='home'), 
    path('buy/<int:id>/', CurHub_App_Views.buy_car, name='buy_car'),
    path('view/info/<int:id>/', CurHub_App_Views.view_info, name='view_info'),
    path('view/cars/brand/<int:brand_id>/', CurHub_App_Views.view_cars_filter_by_brand, name='view_cars_brand'),
]