from django.shortcuts import render  # Импортируем только render

def home_page(request):
    return render(request, 'myapp/home.html')

def data_page(request):
    return render(request, 'myapp/data.html')

def test_page(request):
    return render(request, 'myapp/test.html')