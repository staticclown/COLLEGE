from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('viewteacher/',views.TeacherView.as_view()),
    path('subject/',views.SubjectView.as_view()),
    path('login/',views.LoginView.as_view()),
  #  path('teacherdeletion/<str:pk>',views.fun1,name='delete'),
    path('teacherdeletion/<str:pk>',views.TeacherDeletion.as_view()),

]
