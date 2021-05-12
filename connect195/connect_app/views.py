from django.shortcuts import render
from .models import *

def home(request):
	templateName = 'home.html'
	return render(request, templateName)

def login(request):
	templateName = 'login.html'
	return render(request, templateName)

def register(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password')
		country = request.POST.get('country')
		contact = request.POST.get('contact')
		cname = request.POST.get('cname')
		if request.POST.get('group') == "company":
			company = Company(
				name = username,
				email = email,
				password = password,
				company = cname,
				country = country,
				contact = contact
			)
			company.save()
		else:
			agents = Agent(
				name = username,
				email = email,
				password = password,
				country = country,
				contact = contact
			)
			agents.save()
		templateName = 'login.html'
	else:
		templateName = 'login.html'
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

def blog2(request):
	templateName = 'blog2.html'
	return render(request, templateName)

def blog3(request):
	templateName = 'blog3.html'
	return render(request, templateName)

def blog4(request):
	templateName = 'blog4.html'
	return render(request, templateName)

def gurugram(request):
	templateName = 'gurugram.html'
	return render(request, templateName)

def company(request):
	templateName = 'company.html'
	return render(request, templateName)

def agent(request):
	templateName = 'agent.html'
	return render(request, templateName)
