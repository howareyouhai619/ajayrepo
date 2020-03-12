from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def welcome(request):
    s='<h1 style="color:red" > Welcome to django classes And Django is Nurcery level concept</h1>';
    return HttpResponse(s)
