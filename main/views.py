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
#View for index page
def index(request):
    context = base_context(request)
    context["site_name"] = "Последняя теорема Фарма"  # Строка перед | в title страницы
    context["page_name"] = "Главная"  # Строка после |
    return render(request,'pages/index.html', context)

#View for numeric methods page
def numericMehods(request):
    context = base_context(request)
    context["site_name"] = "Численные методы"
    context["page_name"] = "Главная"
    return render(request, 'pages/numericMethods.html', context)

#View for matrix rules in numeric methods page
def matrixLawOfEquality(request):  
    context = {}
    context["site_name"] = "Численные методы"
    context["page_name"] = "Законы матриц"

    #Get size of array from user input and get it into context
    if request.method == "POST":
        context["n_value"] = range(int(request.POST.get('size', 0)))
        
    #Get list of user input (first matrix) return listArray = ['2','3','5' etc.] 
    listArray = request.POST.getlist('fake_matrix')

    #Get list of user input (second matrix) return listArray = ['2','3','5' etc.] 
    listArray2 = request.POST.getlist('fake_matrix_second')

    #Declaring of first array
    fisrtArray = []

    #Declaring of second array 
    secondArray = []

    
    #Filling first array using listArray. (round(len(listArray)**0.5)) is for correct filling. Saying easy it's size of arrays 
    if len(listArray) != 0:
        for с in range(round(len(listArray)**0.5)):
            fisrtArray.append([0]*round(len(listArray)**0.5))
        count = 0
        for i in range (round(len(listArray)**0.5)):
            for j in range (round(len(listArray)**0.5)):
                fisrtArray[i][j] = int(listArray[count])
                count += 1

    #Filling second array using listArray2
    if len(listArray2) !=0:
        for g in range(round(len(listArray)**0.5)):
            secondArray.append([0]*round(len(listArray)**0.5))
        count1 = 0
        for i in range(round(len(listArray)**0.5)):
            for j in range(round(len(listArray)**0.5)):
                secondArray[i][j] = int(listArray2[count1])
                count1 +=1

    #Declaration of third array
    thirdArray = np.array

    #Converting first and second array to NumPy array
    np.asarray(fisrtArray)
    np.asarray(secondArray)

    #Getting the value of third matrix using multiplication of first and second matrix
    thirdArray = np.dot(fisrtArray, secondArray)

    #Summ of first and second matrix (A+B)
    sumOfFirstAndSecondMatrix = np.add(fisrtArray, secondArray)

    #Result of left side of rule (A+B)*C
    resultOfLeftSide = np.dot(sumOfFirstAndSecondMatrix, thirdArray)

    #Multiplication of first and third matrix (AC)
    multiplicationOfFirstAndThirdMatrix = np.dot(fisrtArray, thirdArray)
    
    #Multiplication of second and third matrix (BC)
    multiplicationOfSecondAndThirdMatrix = np.dot(secondArray, thirdArray)

    #Result of right side of rule = AC + BC
    resultOfRightSide = np.add(multiplicationOfFirstAndThirdMatrix, multiplicationOfSecondAndThirdMatrix)





    #Getting first and second array to context to display on site
    context["firstArray"] = fisrtArray
    context["secondArray"] = secondArray
    context["thirdArray"] = thirdArray
    context["resultOfLeftSide"] = resultOfLeftSide
    context["resultOfRightSide"] = resultOfRightSide
    return render(request, 'pages/matrixlaws.html', context)