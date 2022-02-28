from django.contrib.auth.models import User
from django.db import models
# Create your models here.


class Autor(models.Model):
    nume_autor = models.CharField(max_length=30)
    prenume_autor = models.CharField(max_length=30)
    tara_origine = models.CharField(max_length=30)

    def __str__(self):
        return '%s %s' % (self.prenume_autor, self.nume_autor)


class Biblioteca(models.Model):
    denumire = models.CharField(max_length=100)
    adresa = models.CharField(max_length=100)

    def __str__(self):
        return self.denumire


class Carti(models.Model):
    titlu = models.CharField(max_length=200)
    an_aparitie = models.IntegerField()
    editura = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images", blank=True)
    autor = models.ManyToManyField(Autor)
    biblioteca = models.ManyToManyField(Biblioteca, blank=True)

    def __str__(self):
        return self.titlu
