from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 20

class AuthorDetailView(generic.DetailView):
    model = Author

class BookListView(generic.ListView):
    model = Book
    paginate_by = 20

class BookDetailView(generic.DetailView):
    model = Book

    #not necessary
    def book_detail_view(request, primary_key):
        try:
            book = Book.objects.get(pk=primary_key)
        except Book.DoesNotExist:
            raise Http404('Book does not exist')

        return render(request, 'catalog/book_detail.html', context={'book': book})

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


