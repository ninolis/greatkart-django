# F:\django\GreatKart\carts\urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.cart, name="cart"),
]
