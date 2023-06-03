from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('addstaff/',views.TeacherView.as_view()),
    path('subject/',views.SubjectView.as_view()),
    path('login/',views.LoginView.as_view()),
]
