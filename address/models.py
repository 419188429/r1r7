#coding=utf-8 
from django.db import models

class Author(models.Model):
    Name= models.CharField(max_length=10)
    Age = models.CharField(max_length=10)
    Country = models.CharField(max_length=15)
    

class Book(models.Model):
    Title = models.CharField(max_length=30)
    ISBN = models.CharField(max_length=10)
    authorname = models.CharField(max_length=10)
    AuthorID = models.ForeignKey(Author, related_name='author_book')
    Publisher = models.CharField(max_length=15)
    PublishDate = models.CharField(max_length=12)
    Price = models.CharField(max_length=7)
    


