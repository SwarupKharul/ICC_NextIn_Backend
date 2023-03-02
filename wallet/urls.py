from django.contrib import admin
from django.urls import path, include
from .views import pay, paymenthandler, success, myTickets, buy, getTransactions, convert, cpaymenthandler
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("pay/", pay, name="pay"),
    path("pay/paymenthandler/", paymenthandler, name="paymenthandler"),
    path("success/", success, name="success"),
    path("myTickets/", myTickets, name="myTickets"),

    path("buy/", buy, name="buy"),
    path("get-transactions/", getTransactions, name="getTransactions"),

    path("convert/", convert, name="convert"),
    path("convert/paymenthandler/", cpaymenthandler, name="paymenthandler"),
]
