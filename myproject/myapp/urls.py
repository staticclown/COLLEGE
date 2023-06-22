from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('viewteacher/',views.TeacherView.as_view()),
    path('subject/',views.SubjectView.as_view()),
    path('adminlogin/',views.AdminLoginView.as_view()),
    path('teacherlogin',views.TeacherLoginView.as_view()),
    path('teacherlogin/selection',views.TeacherSelectionview.as_view()),
    path('teacherlogin/division',views.ClassDivisionsview.as_view()),
    path('teacherdeletion/<str:pk>',views.TeacherDeletion.as_view()),
    path('teacherupdation/<str:pk>',views.TeacherUpdation.as_view()),

]
