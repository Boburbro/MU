from django.contrib import admin
from .models import Book, Loan

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'genre', 'quantity', 'available_quantity')
    list_filter = ('genre',)
    search_fields = ('title', 'author', 'isbn')
    
@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'borrow_date', 'return_date', 'status')
    list_filter = ('status', 'borrow_date')
    search_fields = ('user__username', 'book__title')
    date_hierarchy = 'borrow_date'
