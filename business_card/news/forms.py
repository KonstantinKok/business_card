from .models import Article
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'anons', 'text_all', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            'anons': TextInput( attrs={
                'class': 'form-control',
                        'placeholder': 'Анонс статьи'
            }),
            'text_all': Textarea( attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            } ),
            'date': DateTimeInput( attrs={
                'class': 'form-control',
                'placeholder': '01.01.2024'
            } ),
        }
