from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Добро Пожаловать в 3D хранилище</h1><p>Система работает .</p>")