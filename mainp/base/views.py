from queue import Empty
from django.shortcuts import render
empty = ["!"]
# Create your views here.
def login(request):
    return render(request, 'base/login.html')

def reg(request):
       return render(request, 'base/reg.html')

def shift(request):
    return render(request, 'base/shift.html', {

    "empty": empty})

def add(request):
    return render(request, 'base/add.html')