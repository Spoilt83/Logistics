from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Client, Transportist, Package
from .forms import PackageForm


def index(request):
    return render(request, 'pages/index.html')


def packages(request):
    packages = Package.objects.all()
    return render(request, 'packages/packages.html', {'packages': packages})


def create_shipment(request):
    form = PackageForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('packages')
    return render(request, 'packages/create_shipment.html', {'form': form})


def update_shipment(request):
    return render(request, 'packages/update_shipment.html')


def delete_shipment(request):
    return render(request, 'packages/delete_shipment.html')


def packages_sent(request):
    packages = Package.objects.all()
    return render(request, 'pages/packages_sent.html', {'packages': packages})


def packages_asigned(request):
    packages = Package.objects.all()
    return render(request, 'pages/packages_asigned.html', {'packages': packages})
