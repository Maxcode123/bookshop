"""
URL configuration for bookshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from books.views import (
    ListBooksView,
    ShowBookView,
    ListGenresView,
    ListPublishersView,
    ListAuthorsView,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth", include("rest_framework.urls", namespace="rest_framework")),
    path("books/", ListBooksView.as_view(), name="index-books"),
    path("books/<uuid:uuid>", ShowBookView.as_view(), name="show-book"),
    path("genres/", ListGenresView.as_view(), name="index-genres"),
    path("publishers/", ListPublishersView.as_view(), name="index-publishers"),
    path("authors/", ListAuthorsView.as_view(), name="index-authors"),
]
