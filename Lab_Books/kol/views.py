from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from kol.models import Book, HousePublish
from kol.forms import BookForm

def books(request):
    books = Book.objects.all()
    return render(request, "index.html", {"books": books})


def book_details(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404("Book not found")

    return render(request, "book.html",{"book":book})

def add_book(request):
    if request.method == "POST":
        book = BookForm(request.POST)
        if book.is_valid():
            book.save()
            return redirect('books')  # Пренасочување кон листата на книги
    else:
        book = BookForm()

    return render(request, "add_book.html", {"form": book})
