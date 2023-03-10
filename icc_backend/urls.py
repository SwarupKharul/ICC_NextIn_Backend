"""icc_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from .views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index),
    path("api/", include("djoser.urls")),
    path("api/", include("djoser.urls.jwt")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("me/", include("users.urls")),
    path("matches/", include("match.urls")),
    path("razorpay/", include("wallet.urls")),
    path("store/", include("store.urls")),
    path("redoc/", include_docs_urls(title="API Docs")),
    path(
        "docs/",
        get_schema_view(title="API", description="API for the API", version="1.0.0"),
        name="openapi-schema",
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
