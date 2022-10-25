from django.shortcuts import render
# Create your views here.
def base_context(request):
    context = dict()
    context['user'] = request.user
    return context 
def index(request):
    context = {}
    return render(request,'pages/index.html', context)
