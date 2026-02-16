from django.shortcuts import render
from django.http import HttpResponse
from .models import Asset
from .forms import AssetForm
from django.shortcuts import redirect
from django.contrib import messages


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
    # 1. Обрабатываем GET-запрос (показываем пустую форму)
    if request.method == 'GET':
        form = AssetForm()
        return render(request, 'gallery/upload.html', {'form': form})
    
    # 2. Обрабатываем POST-запрос
    if request.method == 'POST':
        form = AssetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Файл успешно загружен!")
            return redirect('home')
        # 3. Если форма НЕ валидна - возвращаем её с ошибками
        else:
            return render(request, 'gallery/upload.html', {'form': form})

 