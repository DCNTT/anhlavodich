from django.shortcuts import render
from .forms import Loginform
from django.views import View
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
# Create your views here.


def Login(request):
    return render(request, 'base/login.html')


class Login(View):
    def get(self, request):
        lF = Loginform
        return render(request, 'base/Login.html', {'Login':lF})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return HttpResponse('Login success!')

        else:
            return HttpResponse('Login fault !!!')
    
