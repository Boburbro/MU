from django.urls import path
from . import views
from .api import check_username
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/<int:pk>/borrow/', views.borrow_book, name='borrow_book'),
    path('my-books/', views.my_books, name='my_books'),
    path('loan/<int:pk>/return/', views.return_book, name='return_book'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('api/check-username/', check_username, name='check_username'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
