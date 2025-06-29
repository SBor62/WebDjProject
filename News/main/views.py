from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import NewsForm
from .models import News

@login_required
def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            return redirect('news_list')  # Изменили 'news' на 'news_list'
    else:
        form = NewsForm()
    return render(request, 'main/add_news.html', {'form': form})

def news_list(request):
    news = News.objects.all().order_by('-published_date')

    # Диагностический вывод
    print(f"\n{'='*50}\nЗапрос от пользователя: {request.user}")
    print(f"Найдено новостей: {news.count()}")
    if news.exists():
        print(f"Пример новости: {news[0].title} (автор: {news[0].author})")

    return render(request, 'main/news.html', {
        'news': news,  # Важно оставить 'news' (а не 'news_list'), чтобы совпадало с шаблоном
        'debug_info': {
            'news_count': news.count(),
            'first_news': news.first() if news.exists() else None
        }
    })
