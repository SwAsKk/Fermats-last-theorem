from multiprocessing import context
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
    form=SizeForm(request.POST)
    if form.is_valid():
        size=form.cleaned_data['size']
    else:
        form=SizeForm(request.POST)
            
    return render(request, 'pages/matrixlaws.html')