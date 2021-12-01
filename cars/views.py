from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from datetime import datetime, timedelta
import json
import threading
from django.conf import settings

# Create your views here.
def home_page(request):
    print('redirected from home page')
    return render(request, 'index.html')

def index_page(request):
    print('index_page rendered')
    return render(request, 'index.html')

def car_page(request):
    return render(request, 'car.html')

def compare_page(request):
    return render(request, "compare.html")