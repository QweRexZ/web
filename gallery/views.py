from django.shortcuts import render
from django.http import HttpResponse
from .models import Asset

#def home(request):
    #return HttpResponse("<h1>Добро Пожаловать в 3D хранилище</h1><p>Система работает .</p>")

def about(request):
     return render(request, 'gallery/about.html')

def home(request):
# all() возвращает хаос.
# order_by('-created_at') сортирует по полю created_at.
# Минус (-) означает "по убыванию" (DESC).
    assets = Asset.objects.all().order_by('-created_at')
    context_data = {
        'page_title': 'Главная Галерея',
        'assets': assets,
}
    return render(request, 'gallery/index.html', context_data)

def upload(request):
     return render(request, 'gallery/upload.html')


 