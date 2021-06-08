from django.urls import  path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('Taxiorder',views.Taxiorder,name='Taxiorder'),
    path('BusOrder',views.Busorder,name='Busorder'),
    path('Trucksorder',views.Trucksorder,name='Trucksorder'),
    path('Driversorder',views.Driversorder,name='Driversorder'),
    path('login',views.admin_login,name='login'),
    path('tables',views.tables,name='tables'),
    path('price',views.price,name='price'),
    path('vip',views.vip,name='vip'),
    path('about',views.about,name='about')
]

