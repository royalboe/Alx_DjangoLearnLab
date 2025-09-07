from django.shortcuts import render
from django.views.generic.detail import DetailView

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login

from .models import Book, Author, Library, Librarian
from .models import Library

# Create your views here.

def list_books(request):
    books = Book.objects.all()
    # template = loader.get_template('list_books.html')
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)
    # return HttpResponse(template.render(context, request))


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context["books"] = self.object.books.all()
    #     return context

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/signup.html'

class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

