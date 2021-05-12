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
