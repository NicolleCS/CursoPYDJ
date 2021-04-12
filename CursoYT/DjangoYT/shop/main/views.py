from django.shortcuts import render, redirect
from main.models import Item
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def homepage(request):
    return render(request, template_name='main/home.html')

def itenspage(request):
    if request.method == 'GET':
        itens = Item.objects.filter(dono_owner=None)
        return render(request, template_name='main/itens.html', context={'itens':itens})
    if request.method == 'POST':
        purchased_item = request.POST.get('purchased-item')    
        if purchased_item:
            purchased_item_object = Item.objects.get(name=purchased_item)
            purchased_item_object.dono_owner = request.user
            purchased_item_object.save()
            messages.success(request, f'OBRIGADO! O PRODUTO { purchased_item_object.name } FOI COMPRADO COM SUCESSO POR { purchased_item_object.price }!')
        return redirect('itens')    

def loginpage(request):
    if request.method == 'GET':
        return render(request, template_name='main/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('itens')
        else:
            return redirect('login')



def registerpage(request):
    if request.method == 'GET':
        return render(request, template_name='main/register.html')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            return redirect('home')
        else:
            return redirect('register')    
    return redirect('register')   

def logoutpage(request):
    logout(request)
    return redirect('home')