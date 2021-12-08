from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
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
from .forms import CommentForm
from .models import Car


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
def car_page(request, model):
    car = get_object_or_404(Car, car_model=model)
    if car:
        return render(request, 'car.html', {'car':car})
        
@login_required
def compare_page(request):
    car_name1 = request.GET.get('car1')
    car_name2 = request.GET.get('car2')
    
    car1 = func.get_car(car_name1)
    car2 = func.get_car(car_name2)
    
    print(car1['power'])
    result = func.compare(car1, car2)
    
    return render(request, "compare.html", {'car1': car1, 'car2': car2, 'result': result})

@login_required
def choose_compare_page(request):
    return render(request, 'choose_compare_page.html')


def car_comment(request, model):
    car = get_object_or_404(Car, car_model=model)
    comments = car.comments.filter(active=True)
    ratings = 0
    average_rating = 0
    if comments:    
        for comment in comments:
            ratings += comment.rating
        average_rating = ratings / len(comments)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, "car_comments.html", {'car': car, 
                                                'comments': comments,
                                                'average_rating': average_rating,
                                                'new_comment':new_comment, 
                                                'comment_form':comment_form})