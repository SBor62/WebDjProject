from django.shortcuts import render

def home_page(request):
    return render(request, 'main/Home.html')

def Page_two(request):
    return render(request, 'main/Page_two.html')

def Page_three(request):  # Убрали лишнюю 'e'
    return render(request, 'main/Page_three.html')

def Page_four(request):
    return render(request, 'main/Page_four.html')
