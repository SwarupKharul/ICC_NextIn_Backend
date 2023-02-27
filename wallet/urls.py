from django.contrib import admin
from django.urls import path, include
from .views import pay, paymenthandler, success
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("pay/", pay, name="pay"),
    path("pay/paymenthandler/", paymenthandler, name="paymenthandler"),
    path("success/", success, name="success"),
]
