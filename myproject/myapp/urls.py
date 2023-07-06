from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('viewteacher/',views.TeacherView.as_view()),
    path('subject/',views.SubjectView.as_view()),
    path('department',views.DepartmentView.as_view()),
    path('adminlogin/',views.AdminLoginView.as_view()),
    path('teacherlogin',views.TeacherLoginView.as_view()),
    path('selectionfinal',views.Finalview.as_view()),
    path('teacherlogin/division',views.ClassDivisionsview.as_view()),
    path('teacherdeletion/<str:pk>',views.TeacherDeletion.as_view()),
    path('teacherupdation/<str:pk>',views.TeacherUpdation.as_view()),
    path('subjectupdation/<str:pk>',views.SubjectUpdation.as_view()),
    path('departmentupdation/<str:pk>',views.DepartmentUpdation.as_view()),
    path('phase1',views.phase1view.as_view()),
    path('phase2',views.phase2view.as_view()),
    path('phasestatus',views.phasestatusview.as_view()),
    path('split',views.split.as_view()),
    path('phaseupdate/<str:pk>',views.Phaseupdate.as_view()),
    path('subselect',views.subselect.as_view()),
    path('phaseview',views.phaseview.as_view()),
    path('teachersubs',views.TeacherSelectionview.as_view()),
]
