from django.shortcuts import render
from django.core.paginator import Paginator
from django.urls import reverse
from .models import Book


def books_view(request):
    template = 'books/books_list.html'
    context = {'books': Book.objects.all()}
    return render(request, template, context)

def date_view(request, date):
    template = 'books/books_list.html'
    next_date = Book.objects.filter(pub_date__gt=date).values('pub_date').first()
    prev_date = Book.objects.filter(pub_date__lt=date).values('pub_date').first()
    redirect_path = reverse('books')
    print(redirect_path)
    context = {
        'books': Book.objects.filter(pub_date=date),
        'next_date': next_date,
        'prev_date': prev_date,
        'puth': redirect_path}
    return render(request, template, context)

# def date_view(request, date):
#     template = 'books/books_list.html'
#     books = Book.objects.all()
#     paginator = Paginator(books, 10)



