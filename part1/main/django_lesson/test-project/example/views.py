from django.shortcuts import render
from django.http import HttpResponse


def example(request):
    return HttpResponse('Salam, Dünya!')


def say_hi_renad(request):
    print('Hal-hazirda yeni olaraq django oyrenir!')
    return HttpResponse('Salam, Renad!')
