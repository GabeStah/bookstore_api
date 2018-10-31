from datetime import date
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100, blank=True, default='')
    last_name = models.CharField(max_length=100, blank=False)
    birth_date = models.DateField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('last_name',)


class Book(models.Model):
    title = models.CharField(max_length=255, blank=False)
    publication_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
