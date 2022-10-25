from django.shortcuts import render
import numpy as np
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
