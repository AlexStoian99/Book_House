from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView, UpdateView
from django.contrib import messages
from book.forms import BooksForm, AuthorForm, LibraryForm, RegisterForm
from book.models import Carti, Autor, Biblioteca


class IndexView(TemplateView):
    template_name = 'book/index.html'


class BooksList(LoginRequiredMixin, generic.ListView):
    login_url = 'login/'
    model = Carti
    template_name = 'book/books_list.html'

    def get_queryset(self):
        books = Carti.objects.all()
        return books


class AuthorsList(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    model = Autor
    template_name = 'book/author_list.html'

    def get_queryset(self):
        authors = Autor.objects.all()
        return authors


class LibraryList(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    model = Biblioteca
    template_name = 'book/library_list.html'


@login_required(login_url='login/')
def create_book(request):
    """
    Function creates a new book
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = BooksForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'OK'})
        else:
            return JsonResponse({'status': 'ERROR', 'message': "please check fields"})

    else:
        form = BooksForm()
    return render(request, 'book/partials/_form_new_book.html', {'books_form': form})


class BooksUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login/'
    model = Carti
    fields = '__all__'
    success_url = "/books_list/"

@login_required(login_url='book/login/')
def create_author(request):
    """
    Function creates a new author
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = AuthorForm(data=request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'OK'})

        else:
            return JsonResponse({'status': 'ERROR', 'message': "please check fields"})

    else:
        form = AuthorForm()
    return render(request, 'book/partials/_form_new_author.html', {'author_form': form})


class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login/'
    model = Autor
    fields = '__all__'
    success_url = "/authors_list"

@login_required(login_url='login/')
def create_library(request):
    """
    Function creates a new library
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = LibraryForm(data=request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'OK'})
        else:
            return JsonResponse({'status': 'ERROR', 'message': "please check fields"})

    else:
        form = LibraryForm()
    return render(request, 'book/partials/_form_new_library.html', {'library_form': form})


class LibraryUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login/'
    model = Biblioteca
    fields = '__all__'
    success_url = "/library_list"

def login_view(request):
    """
    Function represents the login process.
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('book:index')
            else:
                return redirect('book:login')
    else:
        form = AuthenticationForm()
    return render(request, 'book/login.html', {'form': form})


def logout_view(request):
    """
    Function for logout
    :param request:
    :return:
    """
    logout(request)
    return redirect('book:login')


class DeleteBook(UserPassesTestMixin, LoginRequiredMixin, generic.UpdateView):
    login_url = 'login/'
    model = Carti
    success_url = reverse_lazy('book:books_list')
    permission_denied_message = 'You are not a site administrator!'

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return HttpResponse(self.permission_denied_message, status=403)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.POST['delete'] == '0':
            self.object.delete()
            messages.error(request, 'The book has been deleted.')
        return HttpResponseRedirect(self.get_success_url())


class DeleteAuthor(UserPassesTestMixin, generic.UpdateView):
    login_url = 'login/'
    model = Autor
    success_url = reverse_lazy('book:authors_list')
    permission_denied_message = 'You are not a site administrator!'

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return HttpResponse(self.permission_denied_message, status=403)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.POST['delete_author'] == '0':
            self.object.delete()
            messages.error(request, 'The author has been deleted.')
        return HttpResponseRedirect(self.get_success_url())


class DeleteLibrary(UserPassesTestMixin, LoginRequiredMixin, generic.UpdateView):
    login_url = 'login/'
    model = Biblioteca
    success_url = reverse_lazy('book:library_list')
    permission_denied_message = 'You are not a site administrator!'

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return HttpResponse(self.permission_denied_message, status=403)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.POST['delete_library'] == '0':
            self.object.delete()
            messages.error(request, 'The library has been deleted.')
        return HttpResponseRedirect(self.get_success_url())


def register_view(request):
    """
    Creates a register using modal
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # log the user
            return JsonResponse({'status': 'OK'})
        else:
            return JsonResponse({'status': 'ERROR', 'message': "please check fields"})
    else:
        form = RegisterForm()
    return render(request, 'book/modal_register.html', {'register_form': form})