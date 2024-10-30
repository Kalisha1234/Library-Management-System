# from django.contrib import admin
# from .models import Book, Member, Borrow

# admin.site.register(Book)
# admin.site.register(Member)
# admin.site.register(Borrow)

from django.contrib import admin
from .models import Book, Member, Borrow

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'available_copies')

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'membership_number')

@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ('book', 'member', 'borrow_date', 'return_date')