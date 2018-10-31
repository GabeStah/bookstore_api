from datetime import date
from django.db import models


class Author(models.Model):
    #books = models.ManyToManyField(Book)
    birth_date = models.DateField(blank=True)
    first_name = models.CharField(max_length=100, blank=True, default='')
    last_name = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('last_name',)


class Book(models.Model):
    authors = models.ManyToManyField(Author, blank=False)
    publication_date = models.DateField(default=date.today)
    title = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
