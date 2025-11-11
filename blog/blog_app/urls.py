from django.shortcuts import render, redirect
from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.home),
    path("home", view=views.home, name="home"),
    
    path("about", view=views.about, name="about"),
    
    path("articles", view=views.articles, name="articles"),
    path("articles/<int:id>", view=views.view_article, name="view_article")
]