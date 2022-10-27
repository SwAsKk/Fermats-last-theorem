from multiprocessing import context
from pickle import GET
from tkinter import N
from urllib import request
from django.shortcuts import render
import numpy as np

from main.forms import SizeForm

# Create your views here.
def base_context(request):
    context = dict()
    context['user'] = request.user
    return context 
def index(request):
    context = base_context(request)
    context["site_name"] = "Последняя теорема Фарма"  # Строка перед | в title страницы
    context["page_name"] = "Главная"  # Строка после |
    return render(request,'pages/index.html', context)


def numericMehods(request):
    context = base_context(request)
    context["site_name"] = "Численные методы"
    context["page_name"] = "Главная"
    return render(request, 'pages/numericMethods.html', context)


def matrixLawOfEquality(request):  
    n = 5     
    return render(request, 'pages/matrixlaws.html',{'n_value':range(n)})