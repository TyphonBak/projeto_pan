from django.shortcuts import render

def login(request):
    return render(request, "login.html")

def index(request):
    
    context = {
        'title': 'Sabadin - Index',
        'setor': 'Inicio'
    }

    return render(request, "index.html", context)
