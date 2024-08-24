# Django CRUD Operations

## Create
```python
>>> from bookshelf.models import Book
>>> book = Book(title="1984", author="George Orwell", publication_year=1949)
>>> book.save()
>>> print(f"Book created with ID: {book.id}")
Book created with ID: 1
##Read
>>> book = Book.objects.get(id=1)
>>> print(f"Title: {book.title}")
Title: 1984
>>> print(f"Author: {book.author}")
Author: George Orwell
>>> print(f"Publication Year: {book.publication_year}")
Publication Year: 1949
##Update
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> print(f"Updated title: {book.title}")
Updated title: Nineteen Eighty-Four
##Delete
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> print("Book deleted")
Book deleted
>>> remaining_books = Book.objects.all()
>>> print(f"Remaining books: {list(remaining_books)}")
Remaining books: []
