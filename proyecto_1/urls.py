#from django.conf.urls import url

from django.urls import path
from . import views

urlpatterns = [
    path('inicio', views.index, name='index'),
    path('home', views.menu2,name='menu2'),
    path('magia', views.mostrar, name='mostrar')

]