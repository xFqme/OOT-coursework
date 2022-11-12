from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse 

# Create your views here.
def index(request):
	templates=loader.get_template('main_index.html')
	return HttpResponse(templates.render())

def pg2(request):
	templates=loader.get_template('pg2.html')
	return HttpResponse(templates.render())

def back_mainmenu(reqest):
	return HttpResponseRedirect(reverse('main_index'))
