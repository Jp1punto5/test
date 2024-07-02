#from django.conf.urls import url

from django.urls import path
from . import views

urlpatterns = [
    path('Inicio', views.index, name='index'),
    path('Home', views.menu2,name='menu2'),
    path('Magia', views.mostrar, name='mostrar')

]