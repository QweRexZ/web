from django.shortcuts import render
from django.http import HttpResponse
from .models import Asset

#def home(request):
    #return HttpResponse("<h1>Добро Пожаловать в 3D хранилище</h1><p>Система работает .</p>")

def about(request):
     return render(request, 'gallery/about.html')

def home(request):

    assets = Asset.objects.all()
    context_data = {
    'page_title': 'Главная Галерея',
    'assets': assets, # Передаем реальный QuerySet (список)
}
    return render(request, 'gallery/index.html', context_data)

   

 