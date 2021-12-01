"""carcomparing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cars.views import index_page, home_page, car_page, compare_page, choose_compare

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('index/', index_page, name='index'),
    path('car/', car_page, name="car"),
    path('compare/', compare_page, name="compare"),
    path('choose_compare/', choose_compare, name="choose compare"),
]
