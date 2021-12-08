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
import cars.func as func


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
    car_name1 = request.GET.get('car1')
    car_name2 = request.GET.get('car2')
    
    car1 = func.get_car(car_name1)
    car2 = func.get_car(car_name2)
    
    return render(request, "compare.html", {'car1': car1, 'car2': car2})

@login_required
def choose_compare_page(request):
    return render(request, 'choose_compare_page.html')