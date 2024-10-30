from django.shortcuts import render, redirect
from .models import Book, Member, Borrow
from .forms import BorrowForm

def home(request):
    return render(request, 'library/home.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def member_list(request):
    members = Member.objects.all()
    return render(request, 'library/member_list.html', {'members': members})

# def borrow_book(request):
#     if request.method == 'POST':
#         form = BorrowForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('book_list')
#     else:
#         form = BorrowForm()
#     return render(request, 'library/borrow_book.html', {'form': form})

def borrow_book(request):
    if request.method == 'POST':
        form = BorrowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to the book list or another appropriate page
    else:
        form = BorrowForm()
    return render(request, 'library/borrow_book.html', {'form': form})