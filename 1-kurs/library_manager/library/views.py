from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone
from .models import Book, Loan
from .forms import CustomUserCreationForm

def home(request):
    query = request.GET.get('q')
    genre = request.GET.get('genre')
    books = Book.objects.all()

    if query:
        books = books.filter(Q(title__icontains=query) | Q(author__icontains=query))
    
    if genre and genre != 'all':
        books = books.filter(genre=genre)

    context = {
        'books': books,
        'genre': genre
    }
    return render(request, 'library/book_list.html', context)

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Xush kelibsiz, {user.first_name}!")
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'auth/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Xush kelibsiz, {user.username}!")
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "Tizimdan chiqdingiz.")
    return redirect('login')

@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # Check if user already has an active loan for this book
    active_loan = Loan.objects.filter(user=request.user, book=book, status='active').first()
    
    context = {
        'book': book,
        'active_loan': active_loan
    }
    return render(request, 'library/book_detail.html', context)

@login_required
def my_books(request):
    loans = Loan.objects.filter(user=request.user).order_by('-borrow_date')
    return render(request, 'library/my_books.html', {'loans': loans})

@login_required
def borrow_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if book.available_quantity > 0:
        # Check if already borrowed
        if Loan.objects.filter(user=request.user, book=book, status='active').exists():
            messages.warning(request, "Siz bu kitobni allaqachon olgansiz.")
        else:
            Loan.objects.create(user=request.user, book=book)
            messages.success(request, "Kitob muvaffaqiyatli ijaraga olindi. 14 kun ichida qaytaring.")
    else:
        messages.error(request, "Kechirasiz, bu kitob hozir mavjud emas.")
    
    return redirect('book_detail', pk=pk)

@login_required
def return_book(request, pk):
    loan = get_object_or_404(Loan, pk=pk, user=request.user, status='active')
    loan.status = 'returned'
    loan.actual_return_date = timezone.now()
    loan.save()
    messages.success(request, "Kitob qaytarildi.")
    return redirect('my_books')

# Admin Views (Simplified for now, relying on Django Admin or custom simple views later if requested)
# The prompt requested Admin Dashboard. I'll add a simple one.

from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def admin_dashboard(request):
    total_books = Book.objects.count()
    active_loans = Loan.objects.filter(status='active').count()
    overdue_loans = Loan.objects.filter(status='active', return_date__lt=timezone.now()).count() # Approximation
    
    context = {
        'total_books': total_books,
        'active_loans': active_loans,
        'overdue_loans': overdue_loans,
    }
    return render(request, 'admin/dashboard.html', context)
