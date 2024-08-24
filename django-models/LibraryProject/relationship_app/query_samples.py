from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return author.books.all()

def query_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

def query_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian

# Example usage (you can uncomment and run these in a Django shell)
# author = Author.objects.create(name="George Orwell")
# book1 = Book.objects.create(title="1984", author=author)
# book2 = Book.objects.create(title="Animal Farm", author=author)
# library = Library.objects.create(name="City Library")
# library.books.add(book1, book2)
# librarian = Librarian.objects.create(name="John Doe", library=library)

# print("Books by George Orwell:", query_books_by_author("George Orwell"))
# print("Books in City Library:", query_books_in_library("City Library"))
# print("Librarian for City Library:", query_librarian_for_library("City Library"))
