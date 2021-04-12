from django.urls import path
from main import views

urlpatterns = [
    path('home/', views.homepage, name='home'),
    path('itens/', views.itenspage, name='itens'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
    path('register/', views.registerpage, name='register'),
]