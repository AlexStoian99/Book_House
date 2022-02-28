# Third Party Libraries
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

# Project Modules
from book.models import Carti, Biblioteca, Autor


class BooksForm(ModelForm):
    """
    BooksForm will have the fields from ModelQuestion
    """
    class Meta:
        model = Carti
        fields = '__all__'


class AuthorForm(ModelForm):
    """
   AuthorForm will have the fields from ModelQuestion
    """
    class Meta:
        model = Autor
        fields = '__all__'


class LibraryForm(ModelForm):
    """
   AuthorForm will have the fields from ModelQuestion
    """
    class Meta:
        model = Biblioteca
        fields = '__all__'


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

