from django.shortcuts import render
from django.views import ListView, DetailView
from django.template import loader
from django.http import HttpResponse
from .models import Book, Author, Library, Librarian

# Create your views here.

def list_books(request):
    books = Book.objects.all()
    # template = loader.get_template('list_books.html')
    context = {'books': books}
    return render(request, 'list_books.html', context)
    # return HttpResponse(template.render(context, request))


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context["books"] = self.object.books.all()
    #     return context
