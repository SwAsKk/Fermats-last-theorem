"""courseWork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
import imp
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('numericmethods/', views.numericMehods),
    path('numericmethods/matrixrules', views.matrixLawOfEquality),
    path('numericmethods/determinant',views.determinant),
    path('login/', views.LoginView.as_view(), name='login_url'),
    path('logout/', views.logout_view, name='logout_url'),
    path('registration/', views.RegistrView.as_view(), name='reg_url'),
    path('profile/', views.profile),
    path('numericmethods/gauss',views.gauss_method),
    path('quiz/<int:quiz_id>/', views.quiz, name='quiz'),
    path('quiz/<int:quiz_id>/submit/', views.submit_quiz,name='submit_quiz'),
    path('numericmethods/crammer',views.crammer_method),
    
    
]

handler404 = "main.views.page_not_found"
