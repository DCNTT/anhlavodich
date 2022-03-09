from django.shortcuts import render
from django.http import HttpResponse
from .forms import Registerform



def Register(request):
    form = Registerform()
    if request.method == 'POST':
        form = Registerform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Account Register Success !!')
    return render(request, 'base/register.html', {'form':form})



