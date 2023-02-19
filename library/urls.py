from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("gettAllBooks/", views.getAllBooks, name="getAllBooks"),
    path("gettAllMembers/", views.getAllMembers, name="getAllMembers"),
    path("gettAllOrders/", views.getAllOrders, name="getAllOrders"),
]
