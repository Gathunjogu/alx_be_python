# Delete Operation

```python
from bookshelf.models import Book
book = Book.objects.get(id=1)
book.delete()
print("Book deleted")

remaining_books = Book.objects.all()
print(f"Remaining books: {list(remaining_books)}")

