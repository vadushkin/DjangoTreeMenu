from django.shortcuts import render


def home_page(request, name):
    return render(request, 'app_menu/home.html', {'name': name})
