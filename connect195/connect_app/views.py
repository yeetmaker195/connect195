from django.shortcuts import render, redirect
from .models import *


def home(request):
	templateName = 'home.html'
	return render(request, templateName)

def login(request):
	if request.method == 'GET':
		templateName = 'login.html'
		return render(request, templateName)
	else:
		email = request.POST.get('username')
		password = request.POST.get('password')
		user = Agent.objects.get(email=email, password=password)
		request.session['email'] = email
		print(request.session['email'])
		return render(request, 'adminpanel/dashboard.html', {'email':email})

def logout(request):
	if request.method == 'GET':
		request.session.flush()
		print("working")
		return redirect('/login')

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

def dashboard(request):
	templateName = 'adminpanel/dashboard.html'
	return render(request, templateName)

def pipeline(request):
	templateName = 'adminpanel/pipeline.html'
	return render(request, templateName)

def leads(request):
	templateName = 'adminpanel/leads.html'
	leads = Leads.objects.filter().all()
	return render(request, templateName, {'data': leads})

def opportunities(request):
	templateName = 'adminpanel/opportunities.html'
	# opportunities = opportunities.objects.filter().all()
	return render(request, templateName)

def training(request):
	templateName = 'adminpanel/training.html'
	return render(request, templateName)

def application(request):
	templateName = 'adminpanel/application.html'
	return render(request, templateName)

def payments(request):
	templateName = 'adminpanel/payments.html'
	return render(request, templateName)

def helpCenter(request):
	templateName = 'adminpanel/helpcenter.html'
	return render(request, templateName)

def editprofile(request):
	templateName = 'adminpanel/editprofile.html'
	agent = Agent.objects.get(email=request.session['email'])
	return render(request, templateName, {'data': agent})	

def addLead(request):
	templateName = 'adminpanel/leads.html'
	if request.method == 'POST':
		name = request.POST.get('name')
		job = request.POST.get('job')
		phone = request.POST.get('phone')
		contact = request.POST.get('contact')
		comment = request.POST.get('comment')
		agent = Agent.objects.get(email=request.session['email'])
		lead = Leads(
			name = name,
			contact = contact,
			job_title = job,
			note = comment,
			created_by = agent
		)
		lead.save()
		message = "Leads created successfully!"
	return render(request, templateName, {'message': message})

def addopportunities(request):
	templateName = 'adminpanel/opportunities.html'
	# if request.method == 'POST':
	# 	Industries = request.POST.get('industries')
	# 	Company = request.POST.get('company')
	# 	Country = request.POST.get('country')
	# 	BusinessType = request.POST.get('businesstype')
	# 	Commission = request.POST.get('commission')
	# 	other = request.POST.get('other')
	# 	agent = Agent.objects.get(email=request.session['email'])
	# 	opportunities = opportunities(
	# 		Industries = industries,
	# 		Company = company,
	# 		Country = country,
	# 		BusinessType = businesstype,
	# 		Commission = commission,
	# 		other = other,
	# 		created_by = agent
	# 	)
	# 	opportunities.save()
	return render(request, templateName, {'message': "message"})

def addeditprofile(request):
	templateName = 'adminpanel/editprofile.html'
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('EmailID')
		contact = request.POST.get('mobileno')
		country = request.POST.get('country')
		agent = Agent.objects.get(email=request.session['email'])
		editprofile = Agent(
			name = name,
			Country = Country,
			email = emailid,
			contact = mobileno
		)
		editprofile.save()
	return render(request, templateName, {'message': "message"})




