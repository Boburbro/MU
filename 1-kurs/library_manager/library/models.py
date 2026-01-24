from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class Book(models.Model):
    GENRE_CHOICES = [
        ('fiction', 'Badiiy'),
        ('science', 'Ilmiy'),
        ('documentary', 'Hujjatli'),
        ('history', 'Tarixiy'),
        ('other', 'Boshqa'),
    ]

    title = models.CharField(max_length=200, verbose_name="Kitob nomi")
    author = models.CharField(max_length=200, verbose_name="Muallif")
    isbn = models.CharField(max_length=13, unique=True, verbose_name="ISBN")
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES, default='other', verbose_name="Janr")
    description = models.TextField(blank=True, verbose_name="Tavsif")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Jami soni")
    image = models.ImageField(upload_to='books/', blank=True, null=True, verbose_name="Rasm")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def available_quantity(self):
        active_loans = self.loan_set.filter(status='active').count()
        return self.quantity - active_loans

class Loan(models.Model):
    STATUS_CHOICES = [
        ('active', 'Ijarada'),
        ('returned', 'Qaytarilgan'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Kitob")
    borrow_date = models.DateTimeField(auto_now_add=True, verbose_name="Olingan vaqt")
    return_date = models.DateTimeField(verbose_name="Qaytarish muddati") # Expected return date
    actual_return_date = models.DateTimeField(null=True, blank=True, verbose_name="Qaytarilgan vaqt")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active', verbose_name="Holat")

    def save(self, *args, **kwargs):
        if not self.id and not self.return_date:
            self.return_date = timezone.now() + timedelta(days=14)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"
