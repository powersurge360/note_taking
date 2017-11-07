from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Note(models.Model):
    body = models.TextField()
    title = models.CharField(max_length=100, null=True, blank=True)
    book = models.ForeignKey(Book, related_name='notes')

    def __str__(self):
        return self.title
