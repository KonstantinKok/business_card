from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.generic.edit import DeleteView


def news_home(request):
    news = Article.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news':news})

class NewsDeleteView(DeleteView):
    model = Article
    template_name = 'news/details_view.html'
    context_object_name = 'article'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма заполнена не верно'
    form = ArticleForm()
    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'news/create.html', data)
