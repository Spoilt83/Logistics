from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('packages', views.packages, name='packages'),
    path('packages_sent', views.packages_sent, name='packages_sent'),
    path('packages_asigned', views.packages_asigned, name='packages_asigned'),
]