from users.models import UserProfile
from books.models import Book

def create_users():
    user1 = UserProfile.objects.create_user(username='user1', email='user1@gmail.com', password='234567', APIkey='1234567890', balance=100)
    user2 = UserProfile.objects.create_user(username='user2', email='user2@gmail.com', password='234567', APIkey='2345678', balance=200)
    user3 = UserProfile.objects.create_user(username='user3', email='user3@gmail.com', password='234567', APIkey='567234', balance=300)
    return {
        'user1': user1,
        'user2': user2,
        'user3': user3,
    }

def create_book_data():
    book1 = Book.objects.create(title='book1', isbn='book1-isbn-1', author='book 1 author', publisher='book 1 publisher')
    book2 = Book.objects.create(title='book2', isbn='book2-isbn-2', author='book 2 author', publisher='book 2 publisher')
    book3 = Book.objects.create(title='book3', isbn='book3-isbn-3', author='book 3 author', publisher='book 3 publisher')
    book4 = Book.objects.create(title='book4', isbn='book4-isbn-4', author='book 4 author', publisher='book 4 publisher')
    book5 = Book.objects.create(title='book5', isbn='book5-isbn-5', author='book 5 author', publisher='book 5 publisher')
    
    return {
        'book1': book1,
        'book2': book2,
        'book3': book3,
        'book4': book4,
        'book5': book5,
    }