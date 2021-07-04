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
    created_by = models.ForeignKey(Agent, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class opportunities(models.Model):
    industries = models.CharField(max_length=255)
    Company = models.CharField(max_length=255, null=True)
    bussinesstype = models.CharField(max_length=255)
    commission = models.CharField(max_length=255)
    Country = models.CharField(max_length=255)
    other = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Agent, on_delete=models.CASCADE)

    def __str__(self):
        return self.commission
     




