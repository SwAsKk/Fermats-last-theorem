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
    context = {}
    context["site_name"] = "Численные методы"
    context["page_name"] = "Законы матриц"
    #firstArray = np.array(((2,2)), dtype="int32")
    if request.method == "POST":
        context["n_value"] = range(int(request.POST.get('size', 0)))
        
    if request.POST.get('size') != 0:
            sizeOfArray = int(request.POST.get('size', 0))
    print(sizeOfArray)
      
    listArray = request.POST.getlist('fake_matrix')
    fisrtArray = []
    
    
    if len(listArray) != 0:
        for с in range(round(len(listArray)**0.5)):
            fisrtArray.append([0]*round(len(listArray)**0.5))
        count = 0
        for i in range (round(len(listArray)**0.5)):
            for j in range (round(len(listArray)**0.5)):
                fisrtArray[i][j] = int(listArray[count])
                count += 1

    print(fisrtArray)
    
    #for i in range(2):
        #for j in range(2):
            #firstArray[i][j].insert(firstArray,listArray)
    print(listArray) 
    context["firstArray"] = fisrtArray
    
    return render(request, 'pages/matrixlaws.html', context)