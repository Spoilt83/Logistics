from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_shipment', views.create_shipment, name='create_shipment'),
    path('update_shipment/<int:id>', views.update_shipment, name='update_shipment'),
    path('delete_shipment/<int:id>', views.delete_shipment, name='delete_shipment'),
    path('packages', views.packages, name='packages'),
    path('packages_sent', views.packages_sent, name='packages_sent'),
    path('packages_asigned', views.packages_asigned, name='packages_asigned'),
]