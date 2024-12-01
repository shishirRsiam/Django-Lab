from . import helper
from django.db import models
from Authenticator_App.models import User 

class Categorie(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='Library_App/categories')

    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=500)
    description = models.TextField(null=1)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    available_copies = models.IntegerField(default=1)
    img = models.ImageField(upload_to='Library_App/books')
    categories = models.ManyToManyField(Categorie)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}, {self.author}'

class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrowed')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrowed_books')
    
    price = models.DecimalField(max_digits=10, decimal_places=2, null=1)
    after_balance = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    transaction_id = models.CharField( 
        max_length=100, default=helper.generate_transaction_id, editable=0)

    is_returned = models.BooleanField(default=False, null=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)