# Retrieve Operation

```python
from bookshelf.models import Book
book = Book.objects.get(id=1)
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")