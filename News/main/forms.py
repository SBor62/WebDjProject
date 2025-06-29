from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content']  # Поля, которые будет заполнять пользователь
        # author автоматически подставится при сохранении