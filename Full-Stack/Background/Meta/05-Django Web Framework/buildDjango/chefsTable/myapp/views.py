from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from datetime import datetime

from myapp.forms import LogForm

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

def menuitems(request,dish):
    items = {
        'pasta': 'A delicious Italian dish.',
        'falafel': 'A delicious Lebanese dish.',
        'cheesecake': 'A delicious American dessert'
    }
    
    description = items[dish]
    
    return HttpResponse(f"<h2> {dish} </h2>" + description)

def form_view(request):
    form = LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form":form}
    return render(request, "home.html", context)