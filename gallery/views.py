from django.shortcuts import render
from django.http import HttpResponse

#def home(request):
    #return HttpResponse("<h1>Добро Пожаловать в 3D хранилище</h1><p>Система работает .</p>")

def about(request):
     return render(request, 'gallery/about.html')

def home(request):

    fake_database = [
        {'id': 1, 'name': 'Sci-Fi Helmet', 'file_size': '15 MB'},
        {'id': 2, 'name': 'Old Chair', 'file_size': '2 MB'},
        {'id': 3, 'name': 'Cyber Truck', 'file_size': '10 MB'},
        {'id': 4, 'name': 'Plane', 'file_size': '12 MB'},
    ]

    context_data = {
        'page_title': 'Главная Галерея',
        'assets': fake_database,
    }
    
    return render(request, 'gallery/index.html', context_data)
 