from django.contrib import admin
from django.urls import path, include
from .views import pay, paymenthandler, success, myTickets
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("pay/", pay, name="pay"),
    path("pay/paymenthandler/", paymenthandler, name="paymenthandler"),
    path("success/", success, name="success"),
    path("myTickets/", myTickets, name="myTickets"),
]
