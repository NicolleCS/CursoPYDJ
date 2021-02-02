from django.shortcuts import render
from main.models import Item

def homepage(request):
    return render(request, template_name='main/home.html')

def itenspage(request):
    itens = Item.objects.all()
    return render(request, template_name='main/itens.html', context={'itens':itens})

def loginpage(request):
    return render(request, template_name='main/login.html', context={})

def registerpage(request):
    return render(request, template_name='main/register.html', context={})
