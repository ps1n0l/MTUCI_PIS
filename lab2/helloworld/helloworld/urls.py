from ast import pattern

from django import urls
from django.contrib import admin
from django.urls import include, path
from flatpages import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hello/", views.home, name="hello"),
    path("admin/", admin.site.urls)
]
