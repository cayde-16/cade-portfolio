from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path("", views.home, name="home"),
    path("post/", views.post, name="post"),
    # path('send_email/', views.sendEmail, name="send_email")
]