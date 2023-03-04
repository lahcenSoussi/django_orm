from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',Home),
    path('index/',Index),
    path('categories/',List_catgs,name='catgs'),
    path('categories/create',Create_catg),
    path('courses/',List_courses),
    path('profs/',List_profs),
]
