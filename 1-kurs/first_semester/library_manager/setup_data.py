import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from library.models import Book
from django.core.files import File

def create_data():
    # Create Superuser
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print("Superuser 'admin' created (password: admin123)")

    # Create Student
    if not User.objects.filter(username='student').exists():
        user = User.objects.create_user('student', 'student@example.com', 'student123')
        print("User 'student' created (password: student123)")

    # Create Books
    if Book.objects.count() == 0:
        Book.objects.create(
            title='O‘tkan kunlar',
            author='Abdulla Qodiriy',
            isbn='9789943021234',
            genre='fiction',
            description='Oʻzbek adabiyotining birinchi romani.',
            quantity=5
        )
        Book.objects.create(
            title='Sapiens: Insoniyatning qisqacha tarixi',
            author='Yuval Noah Harari',
            isbn='9780099590088',
            genre='history',
            description='Insoniyat tarixi haqida qiziqarli asar.',
            quantity=3
        )
        Book.objects.create(
            title='Stiv Jobs',
            author='Walter Isaacson',
            isbn='9781451648539',
            genre='documentary',
            description='Apple asoschisi Stiv Jobsning tarjimai holi.',
            quantity=2
        )
        print("3 sample books created.")
    else:
        print("Books already exist.")

if __name__ == '__main__':
    create_data()
