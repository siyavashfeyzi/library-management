from django.db import models
from datetime import datetime, timedelta
# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.PositiveIntegerField()


class Member(models.Model):
    fristName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)


def expiry():
    return datetime.today() + timedelta(days=14)


class Order(models.Model):
    member = models.ForeignKey(Member, on_delete=models.PROTECT)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    orderedDate = models.DateField(auto_now_add=True)
    expiryDate = models.DateField(default=expiry)
    recovered = models.BooleanField(default=False)
