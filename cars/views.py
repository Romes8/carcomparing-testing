from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from datetime import datetime, timedelta
import json
import threading
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def home_page(request):
    print('redirected from home page')
    return render(request, 'login.html')

@login_required
def index_page(request):
    print('index_page rendered')
    return render(request, 'index.html')


def logout_page(request):
    try:
        logout(request)
        print('logout_page')
    except KeyError:
        pass
    return render(request, 'login.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user:
            login(request, user=user)
            print('user logged in')
            return redirect('/index/')
        else:
            print("user not logged in")
            return redirect('login')

    return render(request, "login.html")

@login_required
def car_page(request):
    return render(request, 'car.html')

@login_required
def compare_page(request):
    return render(request, "compare.html")

@login_required
def choose_compare_page(request):
    return render(request, 'choose_compare_page.html')