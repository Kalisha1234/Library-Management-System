from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('members/', views.member_list, name='member_list'),
    path('borrow_book/', views.borrow_book, name='borrow_book'),
]