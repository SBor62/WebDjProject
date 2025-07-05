# main/forms.py
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age', 'phone_number')
        labels = {
            'username': 'Имя пользователя',
            'email': 'Электронная почта',
            'age': 'Возраст',
            'phone_number': 'Номер телефона',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            existing_classes = field.widget.attrs.get('class', '')
            classes = existing_classes + ' form-control'
            field.widget.attrs['class'] = classes.strip()
