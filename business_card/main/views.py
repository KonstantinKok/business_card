from django.shortcuts import render
from django.template.defaultfilters import title


def home(request):
    data_home = {
        'title': 'Главная страница',
    }
    return render(request, 'main/home.html', data_home)


def about(request):
    data_about = {
        'title': 'Мои достижения',
    }
    return render(request, 'main/about.html', data_about)


def my_projects(request):
    data_projects = {
        'title': 'Мои проекты'
    }
    return render(request, 'main/my_projects.html', data_projects)


def contacts(request):
    data_contacts = {
        'title': 'Контакты',
    }
    return render(request, 'main/contacts.html', data_contacts)
