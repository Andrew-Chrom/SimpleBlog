# from django.shortcuts import render
from django.urls import path
from . import views


urlpatterns = [
    path("articles/", view=views.ArticlesListCreate.as_view(), name="articles-view-create"),
    path("articles/<int:pk>", view=views.ArticlesRetrieveUpdateDestroy.as_view(), name="update")
]