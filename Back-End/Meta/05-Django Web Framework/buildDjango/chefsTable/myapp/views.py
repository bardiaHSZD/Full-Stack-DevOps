from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from datetime import datetime

def say_hello(request):
    return HttpResponse('Hello World')

def homepage(request):
    return HttpResponse("Welcome to Little Lemon!")

def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)

def menu(request):
    text = """<h1 style="color: #F4CE14;"> This is Little Lemon again!</h>"""
    return HttpResponse(text)  
