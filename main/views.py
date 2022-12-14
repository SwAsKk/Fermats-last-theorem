from multiprocessing import context
from pickle import GET
from tkinter import N
from urllib import request
from django.shortcuts import render
import numpy as np
from numpy import linalg

from main.forms import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.views import View

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



class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', context={'form': form})


    def post(self, request):
        bound_form = LoginForm(request.POST)

        if bound_form.is_valid():
            login_user = bound_form.cleaned_data['login']
            password = bound_form.cleaned_data['password']

            user = authenticate(username=login_user, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/')

        return render(request, 'login.html', context={'form':bound_form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


class RegistrView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', context={'form': form})

    def post(self, request):
        bound_form = RegisterForm(request.POST)

        if bound_form.is_valid():
            new_user = bound_form.save_user()
            if (request.user.is_staff):
                return render(request, 'index.html')
            else:
                return HttpResponseRedirect('/')

        return render(request, 'register.html', context={'form': bound_form})


def profile(request):
    context = base_context(request)
    context["site_name"] = "Личный кабинет"
    return render (request,'personal.html',context)


#View for numeric methods page
def numericMehods(request):
    context = base_context(request)
    context["site_name"] = "Численные методы"
    context["page_name"] = "Главная"
    return render(request, 'pages/numericMethods.html', context)


#View for finding determinant of matrix in numerical methods
def determinant(request):
    context={}
    context["site_name"] = "Численные методы"
    context["page_name"] = "Определитель матрицы"
    if request.method == "POST":
        context["n_value"] = range(int(request.POST.get('size', 0)))

    listArrayDeterminant = request.POST.getlist('fake_matrix')
    arrayDeterminant = []

    if len(listArrayDeterminant) != 0:
        for с in range(round(len(listArrayDeterminant)**0.5)):
            arrayDeterminant.append([0]*round(len(listArrayDeterminant)**0.5))
        count = 0
        for i in range (round(len(listArrayDeterminant)**0.5)):
            for j in range (round(len(listArrayDeterminant)**0.5)):
                arrayDeterminant[i][j] = int(listArrayDeterminant[count])
                count += 1

    np.asarray(arrayDeterminant)


    if len(arrayDeterminant) != 0 :
        determinant = linalg.det(arrayDeterminant).round
        

        context["arrayDeterminant"] = arrayDeterminant
        context["determinant"] = determinant
        print(determinant)

    return render(request,'pages/determinant.html',context)

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
    thirdArray = np.ones(2, dtype=np.int64)

    #Converting first and second array to NumPy array
    np.asarray(fisrtArray)
    np.asarray(secondArray)

    if len(fisrtArray) != 0 :
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