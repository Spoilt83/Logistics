from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'pages/index.html')


def packages(request):
    return render(request, 'packages/packages.html')


def packages_sent(request):
    return render(request, 'pages/packages_sent.html')


def packages_asigned(request):
    return render(request, 'pages/packages_asigned.html')
