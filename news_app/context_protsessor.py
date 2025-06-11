from django.shortcuts import render
from unicodedata import category

from .models import News, FooterData, Category


def FooterView(request):
    footer  = FooterData.objects.all()

    jahon = News.objects.filter(category__name="Jahon")[0]
    jahon2 = News.objects.filter(category__name="Jahon")[1]
    jahon3 = News.objects.filter(category__name="Jahon")[2]

    context = {
        'footer': footer,
        'jahon': jahon,
        'jahon2': jahon2,
        'jahon3': jahon3

    }

    return context
