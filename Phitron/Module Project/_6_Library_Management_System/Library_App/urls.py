from django.urls import path
from Authenticator_App import views as Authenticator_App_Views
from . import views as Library_App_Views

urlpatterns = [
    path('', Library_App_Views.home, name='home'),
    path('view/book/<int:id>/', Library_App_Views.view_book, name='view_book'),
    path('view/books/<int:category_id>/', Library_App_Views.view_books_filter_by_category, name='view_category'),
    path('view/books/<int:category_id>/', Library_App_Views.view_books_filter_by_category, name='category_books'),
    path('borrow/book/<int:id>/', Library_App_Views.borrow_book, name='borrow_book'),
    path('add/funds/', Library_App_Views.add_funds, name='add_funds'),
    path('return/book/<int:borrow_id>/', Library_App_Views.return_book, name='return_book'),
]
