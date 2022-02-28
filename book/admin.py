# Third Party Libraries
from django.contrib import admin, messages
from django.contrib.auth.models import User
from django.utils import timezone

from .models import Autor, Carti, Biblioteca


class AutorAdmin(admin.ModelAdmin):
    list_display = ('nume_autor', 'prenume_autor', 'tara_origine')


class BibliotecaAdmin(admin.ModelAdmin):
    list_display = ('denumire', 'adresa')


class CartiAdmin(admin.ModelAdmin):
    list_display = ('titlu', 'an_aparitie', 'editura')


admin.site.register(Autor, AutorAdmin)
admin.site.register(Biblioteca, BibliotecaAdmin)
admin.site.register(Carti, CartiAdmin)
admin.site.site_header = 'Book House'
