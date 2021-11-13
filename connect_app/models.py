from django.db import models

# Create your models here.
class Agent(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    contact = models.CharField(max_length=255, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Company(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    contact = models.CharField(max_length=255, null=True)
    company = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Leads(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255, null=True)
    job_title = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    note = models.CharField(max_length=255, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    created_by_agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True)
    created_by_company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

class AddTask(models.Model):
    Task_title = models.CharField(max_length=255, null=True)
    Description = models.CharField(max_length=255, null=True)
    Due_date = models.DateField(max_length=255, null=True)
    leads = models.ForeignKey(Leads, on_delete=models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by_agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.Task_title

class LeadAction(models.Model):
    Value = models.CharField(max_length=255, null=True)
    Estimated_close = models.DateField( null=True)
    Confidence = models.CharField(max_length=255, null=True)
    leads = models.ForeignKey(Leads, on_delete=models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by_agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True)


class Accreditation(models.Model):
    accreditation_name = models.CharField(max_length=255)
    accreditation_url = models.CharField(max_length=255, null=True)
    logo = models.ImageField( null=True)
    note = models.TextField(max_length=255, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.accreditation_name        


class LeadsDetails(models.Model):
    min_sal_exp= models.CharField(max_length=255, null=True)
    cust_ques_1= models.TextField(null=True)
    cust_ques_2= models.TextField(null=True)
    cust_ques_3= models.TextField(null=True)
    cust_ques_4= models.TextField(null=True)
    indu_exp_req= models.BooleanField()
    about_the_oportu= models.CharField(max_length=2500, null=True)
    leads_provided= models.CharField(max_length=250, null=True)
    currency= models.CharField(max_length=250, null=True)
    lang_oportunity= models.CharField(max_length=250, null=True)
    desc_sales_process= models.CharField(max_length=250, null=True)
    avg_deal_val= models.CharField(max_length=250, null=True)
    rep_cust_spend= models.CharField(max_length=250, null=True)
    avg_yearly_cust_value= models.CharField(max_length=250, null=True)
    exclusive_territory_available= models.BooleanField()
    excu_terri_value= models.CharField(max_length=250, null=True)
    avg_sales_cycle= models.CharField(max_length=250, null=True)
    payment_terms= models.CharField(max_length=250, null=True)
    customer_type= models.CharField(max_length=250, null=True)
    self_emp_working_with_your_comp= models.CharField(max_length=2500, null=True)   
    self_emp_suited_to_your_oportunity= models.CharField(max_length=2500, null=True)
    about_the_trai_provi_sales_prof= models.CharField(max_length=2500, null=True)
    upload_logo= models.ImageField(upload_to="uploads/", null=True)
    upload_header_img= models.ImageField(upload_to="uploads/", null=True)
    product_gallery= models.ImageField(upload_to="uploads/", null=True)
    video= models.TextField( null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    lead = models.ForeignKey(Leads, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.lead

class CompanyDetails(models.Model):
    skype= models.CharField(max_length=255, null=True)
    web_site= models.CharField(max_length=255, null=True)
    upload_logo= models.ImageField(upload_to="uploads/", null=True)
    linkedin_url= models.URLField(blank=True,null=True)
    short_summary= models.TextField()
    about_your_comp= models.TextField()
    industry= models.CharField(max_length=255, null=True)
    company_size= models.CharField(max_length=255, null=True)
    years_traiding= models.CharField(max_length=255, null=True)
    no_of_customers= models.CharField(max_length=255, null=True)
    facebook_page_url= models.URLField(blank=True, null=True)
    twitter_id= models.URLField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.industry

class FinancialTc(models.Model):
    title = models.CharField(max_length=225, null=True)
    commission = models.CharField(max_length=255, null=True)
    commission_details = models.CharField(max_length=255, null=True)       
    our_industry = models.CharField(max_length=255, null=True)       
    target_industories = models.CharField(max_length=255, null=True)       
    commission_details = models.CharField(max_length=255, null=True)       
    territories = models.CharField(max_length=255, null=True)       
    selling_method = models.CharField(max_length=255, null=True)       
    min_sales_experience_req = models.CharField(max_length=255, null=True)       
    industry_exp_req = models.CharField(max_length=255, null=True)       
    leads_provided = models.CharField(max_length=255, null=True)       
    avg_deal_value = models.CharField(max_length=255, null=True)       
    repeat_cast_spend = models.CharField(max_length=255, null=True)       
    exclusive_territory_avil = models.CharField(max_length=255, null=True)       
    available = models.CharField(max_length=255, null=True)       
    avg_sales_cycle = models.CharField(max_length=255, null=True)       
    payments_terms = models.CharField(max_length=255, null=True)       
    customer_type = models.CharField(max_length=255, null=True)       
    product_and_services = models.CharField(max_length=255, null=True)       
    about_the_opportunity = models.CharField(max_length=2500, null=True)       
    why_self_employed_working_comp = models.TextField(max_length=2500, null=True)       
    what_kind_self_empl_best_to_comp = models.TextField(max_length=2500, null=True)       
    training_support = models.TextField(max_length=2500, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)       
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class AgentDetails(models.Model):
    headline = models.CharField(max_length=255, null=True)
    short_summary = models.TextField(max_length=2500, null=True)
    prof_img = models.ImageField(upload_to="uploads/", null=True)
    company_logo_upload = models.ImageField(upload_to="uploads/", null=True)
    years_of_exp = models.CharField(max_length=255, null=True)
    selling_your_best = models.CharField(max_length=255, null=True)
    your_do_u_sell_to = models.CharField(max_length=255, null=True)
    your_org_struc = models.CharField(max_length=255, null=True)
    what_country_based_in = models.CharField(max_length=255, null=True)
    what_city_based_in = models.CharField(max_length=255, null=True)
    network_of_contact= models.CharField(max_length=255, null=True)
    services_in_your_network= models.CharField(max_length=255, null=True)
    industries_in_your_network= models.CharField(max_length=255, null=True)
    size_company_in_your_network= models.CharField(max_length=255, null=True)
    decision_maker_in_your_network= models.CharField(max_length=255, null=True)
    decision_maker_seniority_in_your_network= models.CharField(max_length=255, null=True)
    mobile= models.IntegerField(null=True)
    skype= models.URLField(max_length=255, null=True)
    web_site= models.URLField(max_length=255, null=True)
    world_region = models.CharField(max_length=255, null=True)
    selected_countries = models.CharField(max_length=255, null=True)
    details_other_territories = models.CharField(max_length=255, null=True)
    industries_product_service_you_sell = models.CharField(max_length=255, null=True)
    industries_of_your_clients = models.CharField(max_length=255, null=True)
    product_sold = models.CharField(max_length=255, null=True)
    products_like_to_sell = models.CharField(max_length=255, null=True)
    what_are_you_ooking_for = models.CharField(max_length=2500, null=True)
    achievents_in_sell = models.CharField(max_length=2500, null=True)
    deciding_to_work_with_a_company= models.CharField(max_length=2500, null=True)
    self_employed_sales_agent= models.CharField(max_length=2500, null=True)
    lang_you_speak= models.CharField(max_length=255, null=True)
    you_all_consider= models.CharField(max_length=255, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.headline

class LeadContact(models.Model):
    lead_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    leads = models.ForeignKey(Leads, on_delete=models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by_agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.lead_name


class LeadOrganisation(models.Model):
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    leads = models.ForeignKey(Leads, on_delete=models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by_agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.email

class Notes(models.Model):
    note = models.TextField(max_length=500)
    leads = models.ForeignKey(Leads, on_delete=models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by_agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.note

class Invoice(models.Model):
    opportunity = models.CharField(max_length=100, null=True)
    Invoice_number = models.CharField(max_length=100, null=True)
    business_name = models.CharField(max_length=100, null=True)
    business_address = models.CharField(max_length=100, null=True)
    business_address2 = models.CharField(max_length=100, null=True)
    business_city = models.CharField(max_length=100, null=True)
    business_state = models.CharField(max_length=100, null=True)
    business_country = models.CharField(max_length=100, null=True)
    business_postal_code = models.CharField(max_length=100, null=True)
    Date = models.DateField(auto_now_add=True, null=True, blank=True)
    comp_business_name = models.CharField(max_length=100)
    comp_business_address = models.CharField(max_length=100)
    comp_business_address2 = models.CharField(max_length=100)
    comp_business_city = models.CharField(max_length=100)
    comp_business_sate = models.CharField(max_length=100)
    comp_business_country = models.CharField(max_length=100)
    comp_business_postal_code = models.CharField(max_length=100)
    Currency = models.CharField(max_length=100)
    Commission_percentage = models.CharField(max_length=100)
    Invoice_due_date = models.DateField(auto_now_add=True, null=True, blank=True)
    Tax_name = models.CharField(max_length=100)
    Tax_percentage = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by_agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.opportunity

class AgentApply(models.Model):
    questions = models.CharField(max_length=225, null=True)
    cover_letter = models.CharField(max_length=255, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by_agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True)
    company_name = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.questions

class AgentAsk(models.Model):
    questions = models.CharField(max_length=225, null=True)
    discriptions = models.TextField(max_length=255, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by_agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True)
    company_name = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.questions

class Training(models.Model):
    video_link = models.URLField(max_length=550, null=True)
    title = models.CharField(max_length=500)
    discription = models.TextField(max_length=2500)
    task_for_agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


