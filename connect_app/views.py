from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User


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
		try:
			user = Agent.objects.get(email=email, password=password)
			user.save()
		except:
			messages.success(request, 'Password or Username is incorrect!!!')
			return redirect('/login/')
		request.session['email'] = email
		return redirect('/dashboard/', {'email':email})

def companylogin(request):
	if request.method == 'GET':
		templateName = 'companylogin.html'
		return render(request, templateName)
	else:
		email = request.POST.get('username')
		password = request.POST.get('password')
		try:
			user = Company.objects.get(email=email, password=password)
			user.save()
		except:
			messages.success(request, 'Password or Username is incorrect!!!')
			return redirect('/companylogin/')
		request.session['email'] = email
		return redirect('/companydashboard/', {'email':email})

def logout(request):
	if request.method == 'GET':
		request.session.flush()
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
			messages.success(request, 'Company is Register Succesfully!!!!')
		else:
			agents = Agent(
				name = username,
				email = email,
				password = password,
				country = country,
				contact = contact
			)
			agents.save()
			messages.success(request, 'Agent is Register Succesfully!!!!')
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

def blogh(request):
	templateName = 'blogh.html'
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
	if 'email' in request.session:
		templateName = 'adminpanel/dashboard.html'
		return render(request, templateName)
	else:
		return redirect('/login/')

def companydashboard(request):
	if 'email' in request.session:
		templateName = 'adminpanel/companydashboard.html'
		return render(request, templateName)
	else:
		return redirect('/companylogin/')
	
def pipeline(request):
	if 'email' in request.session:
		templateName = 'adminpanel/pipeline.html'
		agent = Agent.objects.get(email=request.session['email'])
		idea = Leads.objects.filter(created_by_agent=agent).filter(status='idea')
		contacted = Leads.objects.filter(created_by_agent=agent).filter(status='contacted')
		discovery = Leads.objects.filter(created_by_agent=agent).filter(status='discovery')
		presentation = Leads.objects.filter(created_by_agent=agent).filter(status='presentation')
		closed = Leads.objects.filter(created_by_agent=agent).filter(status='closed')
		return render(request, templateName, {'idea':idea, 'contacted':contacted, 'discovery': discovery, 'presentation': presentation,  'closed':closed})
	else:
		return redirect('/login/')

def companypipeline(request):
	if 'email' in request.session:
		return render(request, 'adminpanel/companypipeline.html')
	else:
		return redirect('/companylogin/')


def leads(request):
	if 'email' in request.session:
		templateName = 'adminpanel/leads.html'
		agent = Agent.objects.get(email=request.session['email'])
		leads = Leads.objects.filter(created_by_agent=agent)
		return render(request, templateName, {'data': leads})
	else:
		return redirect('/login/')

def opportunities(request):
	if 'email' in request.session:
		templateName = 'adminpanel/opportunities.html'
		companydetails = CompanyDetails.objects.all()
		data = CompanyDetails.objects.filter(company_size=10)
		financial = FinancialTc.objects.all()
		if request.method == "get":
				industries = request.GET.get('industries')
				company = request.GET.get('company')
				Country = request.GET.get('Country')
				Business_Type = request.GET.get('Business_Type')
				Commission = request.GET.get('Commission')
				Other = request.GET.get('Other')
				search = (industries,company,Country,Business_Type,Commission,Other)
				if search!=None:
						financial = FinancialTc.objects.filter(our_industry=industries,customer_type=Business_Type,commission=Commission)

		return render(request, templateName, {'companydetails':companydetails, 'financial':financial,'data':data})
	else:
		return redirect('/login/')

def training(request):
	if 'email' in request.session:
		templateName = 'adminpanel/training.html'
		agent = Agent.objects.get(email=request.session['email'])
		print(agent)
		obj = Training.objects.filter(task_for_agent=agent)
		print(obj)
		return render(request, templateName,{'obj':obj})
	else:
		return redirect('/login/')

def application(request):
	if 'email' in request.session:
		templateName = 'adminpanel/application.html'
		return render(request, templateName)
	else:
		return redirect('/login/')

def payments(request):
	if 'email' in request.session:
		templateName = 'adminpanel/payments.html'
		agent = Agent.objects.get(email=request.session['email'])
		inv = Invoice.objects.filter(created_by_agent=agent)
		return render(request, templateName,{'inv':inv})
	else:
		return redirect('/login/')

def helpCenter(request):
	if 'email' in request.session:
		templateName = 'adminpanel/helpcenter.html'
		return render(request, templateName)
	else:
		return redirect('/login/')

def companydetails(request, id):
	templateName = 'adminpanel/companydetails.html'
	company = Company.objects.get(pk=id)
	companydetails = None
	financialtc = None
	try:
		companydetails = CompanyDetails.objects.get(company=company)
	except:
		companydetails = None
	try:
		financialtc = FinancialTc.objects.get(company=company)
	except:
		financialtc = None
	return render(request, templateName, {'data': companydetails,'financialtc':financialtc})
		
def editprofile(request):
	templateName = 'adminpanel/editprofile.html'
	agent = Agent.objects.get(email=request.session['email'])
	agent_details = None
	try:
		agent_details = AgentDetails.objects.get(agent=agent)
	except:
		agent_details=None
	return render(request, templateName, {'data': agent, 'agent_details': agent_details})

def companyeditprofile(request):
	templateName = 'adminpanel/companyeditprofile.html'
	company = Company.objects.get(email=request.session['email'])
	company_details = None
	try:
		company_details = CompanyDetails.objects.get(company=company)
	except:
		company_details=None
	return render(request, templateName, {'data': company, 'agent_details': company_details})

def addLead(request):
	templateName = 'adminpanel/leads.html'
	if request.method == 'POST':
		name = request.POST.get('name')
		job = request.POST.get('job')
		email = request.POST.get('email')
		contact = request.POST.get('contact')
		comment = request.POST.get('comment')
		status = request.POST.get('status')
		agent = Agent.objects.get(email=request.session['email'])
		lead = Leads(
			name = name,
			contact = contact,
			job_title = job,
			email = email,
			note = comment,
			status = status,
			created_by_agent = agent		
		)
		lead.save()
		messages.success(request,"Leads created successfully!")
	return redirect('/leads')

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
	# return render(request, templateName, {'message': "message"})

def addeditprofile(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		contact = request.POST.get('mobileno')
		country = request.POST.get('country')
		agent = Agent.objects.get(email=request.session['email'])
		agent.name = name,
		agent.country = country,
		agent.email = email,
		agent.contact = contact
		agent.save()

		try:
			agentdetails = AgentDetails.objects.get(agent=agent)
			agentdetails.short_summary = request.POST.get('short_summary')
			agentdetails.prof_img = request.POST.get('prof_img')
			agentdetails.company_logo_upload = request.POST.get('company_logo_upload')
			agentdetails.years_of_exp = request.POST.get('years_of_exp')
			agentdetails.selling_your_best = request.POST.get('selling_your_best')
			agentdetails.your_do_u_sell_to = request.POST.get('your_do_u_sell_to')
			agentdetails.your_org_struc = request.POST.get('organizational')
			agentdetails.what_country_based_in = request.POST.get('countries')
			agentdetails.what_city_based_in = request.POST.get('what_city_based_in')
			agentdetails.services_in_your_network = request.POST.get('services_in_your_network')
			agentdetails.industries_in_your_network = request.POST.get('industries'),
			agentdetails.size_company_in_your_network = request.POST.get('company size')
			agentdetails.decision_maker_in_your_network = request.POST.get('network')
			agentdetails.decision_maker_seniority_in_your_network = request.POST.get('seniority')
			agentdetails.skype = request.POST.get('skype')
			agentdetails.web_site = request.POST.get('web_site')
			agentdetails.industries_product_service_you_sell = request.POST.get('product sell')
			agentdetails.industries_of_your_clients = request.POST.get('clients')
			agentdetails.product_sold = request.POST.get('product_sold')
			agentdetails.products_like_to_sell = request.POST.get('products_like_to_sell')
			agentdetails.what_are_you_ooking_for = request.POST.get('short_summary')
			agentdetails.world_region = request.POST.get('world')
			agentdetails.selected_countries = request.POST.get('countries')
			agentdetails.save()
		except:
			agentdetails=None
	return redirect('/editprofile')

def companyaddeditprofile(request):
	if request.method == "POST":
		name = request.POST.get("name")
		company_name = request.POST.get("company") 
		email = request.POST.get("email") 
		contact = request.POST.get("contact") 
		country = request.POST.get("country")
		company = Company.objects.get(email=request.session['email'])
		reg,created = Company.objects.update_or_create(
		name = name,
		email = email,
		contact = contact,
		company = company_name,
		country = country, 
		)
		print(reg)
		print(created)
		reg.save()
		try:
			companydetails = CompanyDetails.objects.get(company=company)
			companydetails.company_size = request.POST.get("company_size") 
			companydetails.Industry = request.POST.get("Industry") 
			companydetails.Years_Traiding = request.POST.get("Years_Traiding") 
			companydetails.no_of_customer = request.POST.get("no_of_customer") 
			companydetails.skype = request.POST.get("skype") 
			companydetails.web_site = request.POST.get("web_site") 
			companydetails.linkedin = request.POST.get("linkedin") 
			companydetails.facebook = request.POST.get("facebook")
			companydetails.twitter = request.POST.get("twitter")
			companydetails.short_summary = request.POST.get("short_summary") 
			companydetails.about_company = request.POST.get("about_company")
			companydetails.save()
		except:
			companydetails = None
		return redirect('/companyeditprofile/')
 

def update_lead(request):
	id = request.POST.get('lead_id')
	status = request.POST.get('status')
	lead = Leads.objects.get(pk=id)
	lead.status = status
	lead.save()
	messages.success(request, "Lead updated successfully!")
	return redirect('/leads')

def leadsupdate(request, id):
	templateName = 'adminpanel/leadsupdate.html'
	leads = Leads.objects.get(pk=id)
	task = AddTask.objects.filter(leads=leads)
	contact = LeadContact.objects.filter(leads=leads)
	organisation = LeadOrganisation.objects.filter(leads=leads)
	note = Notes.objects.filter(leads=leads)
	try:
		leadaction = LeadAction.objects.get(leads=leads)
	except:
		leadaction=None
	return render(request, templateName, {'data':task, 'lead':leads,'leadaction':leadaction,'contact':contact,'organisation':organisation,'note':note})


def tasksave(request):
	if request.method == 'POST':
		tasktitle = request.POST.get('tasktitle')
		comment = request.POST.get('comment')
		date = request.POST.get('date')
		id = str(request.POST.get('leadid'))
		leads = Leads.objects.get(pk=int(id))
		agent = Agent.objects.get(email=request.session['email'])
		task = AddTask(
			Task_title = tasktitle,
			Description = comment,
			Due_date = date,
			leads = leads,
			created_by_agent =agent
		)
		task.save(), 
		messages.success(request, "Task has been Added!")
	return redirect('/leadsupdate/'+str(id)+'/')

def leadaction(request):
	templateName = 'adminpanel/leadsupdate.html'
	if request.method == "POST":
		value = request.POST.get('value')
		confidence = request.POST.get('confidence')
		est_close = request.POST.get('est_close')
		id = str(request.POST.get('leadactionid'))
		leads = Leads.objects.get(pk=int(id))
		agent = Agent.objects.get(email=request.session['email'])
		obj,created = LeadAction.objects.update_or_create(
			Value = value,
			Confidence = confidence,
			Estimated_close = est_close,
			leads = leads,
			created_by_agent =agent,
		)
		print(created)
		print(obj)
		messages.success(request, 'Leadaction is Added!')
	return redirect('/leadsupdate/'+str(id)+'/')

def leadcontact(request):
	if request.method == "POST":
		lead_name = request.POST.get('leadname')
		job_title = request.POST.get('job')
		email = request.POST.get('email')
		contact = request.POST.get('contact')
		id = str(request.POST.get('leadactionid'))
		leads = Leads.objects.get(pk=int(id))
		agent = Agent.objects.get(email=request.session['email'])
		lead = LeadContact(
			lead_name = lead_name,
			job_title = job_title,
			email = email,
			contact = contact,
			leads = leads,
			created_by_agent =agent
		)
		lead.save()			
		messages.success(request, 'LeadContact is Added!')
	return redirect('/leadsupdate/'+str(id)+'/')

def leadorganisation(request):
	if request.method == "POST":
		email = request.POST.get('email')
		contact = request.POST.get('contact')
		id = str(request.POST.get('leadactionid'))
		leads = Leads.objects.get(pk=int(id))
		agent = Agent.objects.get(email=request.session['email'])
		lead = LeadOrganisation(
			email = email,
			contact = contact,
			leads = leads,
			created_by_agent = agent
		)
		lead.save()
		messages.success(request, 'LeadOrganisation is Added!')
	return redirect('/leadsupdate/'+str(id)+'/')

def note(request):
	if request.method == "POST":
		note = request.POST.get('note')
		id = str(request.POST.get('leadactionid'))
		leads = Leads.objects.get(pk=int(id))
		agent = Agent.objects.get(email=request.session['email'])
		lead  = Notes(
			note = note,
			leads = leads,
			created_by_agent = agent
		)
		lead.save()
		messages.success(request, 'Note is Added!')
	return redirect('/leadsupdate/' +str(id)+'/')

def invoice(request):
	if request.method == "POST":
		opportunity = request.POST.get('Opportunity')
		Invoice_number = request.POST.get('Invoice')
		business_name = request.POST.get('Your_business')
		business_address = request.POST.get('business_address')
		business_address2 = request.POST.get('business_address2')
		business_city = request.POST.get('business_city')
		business_state = request.POST.get('business_state')
		business_country = request.POST.get('business_country')
		business_postal_code = request.POST.get('business_code')
		Date = request.POST.get('Date')
		comp_business_name = request.POST.get('Your_business')
		comp_business_address = request.POST.get('business_address')
		comp_business_address2 = request.POST.get('business_address2')
		comp_business_city = request.POST.get('business_city')
		comp_business_sate = request.POST.get('business_state')
		comp_business_country = request.POST.get('business_country')
		comp_business_postal_code = request.POST.get('business_code')
		Currency = request.POST.get('Currency')
		Commission_percentage = request.POST.get('Commission')
		Invoice_due_date = request.POST.get('Invoice_due')
		Tax_name = request.POST.get('Tax_name')
		Tax_percentage = request.POST.get('Tax_percentage')
		agent = Agent.objects.get(email=request.session['email'])
		invoce = Invoice(
			opportunity = opportunity,
			Invoice_number = Invoice_number,
			business_name = business_name,
			business_address = business_address,
			business_address2 = business_address2,
			business_city = business_city,
			business_state = business_state,
			business_country = business_country,
			business_postal_code = business_postal_code,
			Date = Date,
			comp_business_name = comp_business_name,
			comp_business_address = comp_business_address,
			comp_business_address2 = comp_business_address2,
			comp_business_city = comp_business_city,
			comp_business_sate = comp_business_sate,
			comp_business_country = comp_business_country,
			comp_business_postal_code = comp_business_postal_code,
			Currency = Currency,
			Commission_percentage =Commission_percentage,
			Invoice_due_date = Invoice_due_date,
			Tax_name = Tax_name,
			Tax_percentage = Tax_percentage,
			created_by_agent = agent
		)
		invoce.save()
		messages.success(request, 'Invoice is Added!')
	return redirect('/payments')

def agentapply(request):
	if request.method == "POST":
		que = request.POST.get('que')
		letter = request.POST.get('letter')
		agent = Agent.objects.get(email=request.session['email'])
		id = request.POST.get('comid')
		comdetobj = CompanyDetails.objects.get(pk=int(id))
		reg = AgentApply(
			questions=que,
			cover_letter=letter,
			created_by_agent = agent,
			company_name = comdetobj
		)
		reg.save()
	return redirect('/companydetails/' +(id)+'/')

def agentask(request):
	if request.method == "POST":
		que = request.POST.get('que')
		disc = request.POST.get('desc')
		agent = Agent.objects.get(email=request.session['email'])
		id = request.POST.get('comid')
		comdetobj = CompanyDetails.objects.get(pk=int(id))
		reg = AgentAsk(
			questions=que,
			discriptions=disc,
			created_by_agent = agent,
			company_name = comdetobj
		)
		reg.save()
	return redirect('/companydetails/' +(id)+'/')
	

