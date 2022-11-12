from django.urls import path
from . import views

urlpatterns = [
	path ('', views.index, name ='main_index'),
	path ('pg2/', views.pg2, name ='pg2'),
	path ('pg2/back_mainmenu/', views.back_mainmenu, name='backtomain'),
]