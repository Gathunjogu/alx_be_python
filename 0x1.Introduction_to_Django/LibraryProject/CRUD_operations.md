njogu@Gathuu MINGW64 ~/0x1.Introduction_to_Django/LibraryProject (master)
$ python manage.py shell
Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from bookshelf.models import Book
book = Book(title="1984", author="George Orwell", publication_year=1949)
>>> book.save()
>>> print(f"Book created with ID: {book.id}")>>>
Book created with ID: 1
>>> book = Book.objects.get(id=1)
print(f"Title: {book.title}")
>>> print(f"Author: {book.author}")
Title: 1984
>>> print(f"Publication Year: {book.publication_year}")Author: George Orwell
>>>
Publication Year: 1949
>>> book.title = "Nineteen Eighty-Four"
book.save()
>>> print(f"Updated title: {book.title}")>>>
Updated title: Nineteen Eighty-Four
>>> book.delete()
print("Book deleted")
remaining_books = Book.objects.all()
(1, {'bookshelf.Book': 1})
>>> Book deleted
>>> print(f"Remaining books: {list(remaining_books)}")>>>
Remaining books: []
