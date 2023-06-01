from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def fun1(request):
    return HttpResponse('hi')