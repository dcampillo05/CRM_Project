from django.shortcuts import render

def index(request):
    return render(request, 'todos/index.html')

def sobre(request):
    return render(request, 'todos/sobre.html')
