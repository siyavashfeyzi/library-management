from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.


def index(request):
    return render(request, "index.html", {"input": "library"})


def getAllBooks(request):
    query_set = models.Book.objects.all()

    for book in query_set:
        print(book)

    return render(request, "getAllBooks.html", {"Books": query_set})


def getAllMembers(request):
    query_set = models.Member.objects.all()

    for member in query_set:
        print(member)

    return render(request, "getAllMember.html", {"Members": query_set})


def getAllOrders(request):
    query_set = models.Order.objects.all()

    for order in query_set:
        print(order)

    return render(request, "getAllOrders.html", {"Orders": query_set})
