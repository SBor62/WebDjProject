from django.contrib import admin
from .models import News


# main/admin.py
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_author', 'published_date')

    def display_author(self, obj):
        return obj.author.get_full_name() or obj.author.username

    display_author.short_description = 'Автор'


search_fields = ('title', 'content')  # Поиск по этим полям