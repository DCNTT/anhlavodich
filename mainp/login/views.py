from django.shortcuts import render, redirect
from .forms import Loginform
from django.views import View
from django.contrib.auth import authenticate, login , logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
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
            return render(request, 'base/home.html')

        else:
            return HttpResponse('Login fault !!!')

@login_required
def Home(request):
    return render(request, 'base/home.html')

def Logout(request):
    logout(request)
    return redirect('Login')

def test(request):
    return render(request, 'base/test.html')