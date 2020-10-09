from django.shortcuts import render
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import (handler400, handler403, handler404, handler500)
from django.views.generic.base import TemplateView

# Create your views here.
def home(request):
	templateName = 'home.html'
	return render(request, templateName)

def about(request):
	templateName = 'about.html'
	return render(request, templateName)

def team(request):
	templateName = 'team.html'
	return render(request, templateName)

def services(request):
	templateName = 'services.html'
	return render(request, templateName)

def pricing(request):
	templateName = 'pricing.html'
	return render(request, templateName)

def checkout(request):
	templateName = 'checkout.html'
	return render(request, templateName)

def events(request):
	templateName = 'events.html'
	return render(request, templateName)

def contact(request):
	templateName = 'contact.html'
	return render(request, templateName)

def blog(request):
	templateName = 'blog.html'
	return render(request, templateName)

def blog1(request):
	templateName = 'blog1.html'
	return render(request, templateName)

def gurugram(request):
	templateName = 'gurugram.html'
	return render(request, templateName)
