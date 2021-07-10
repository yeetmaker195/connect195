from django.contrib import admin
from .models import *

admin.site.register(Agent)
admin.site.register(Company)
admin.site.register(Leads)
admin.site.register(LeadsDetails)
admin.site.register(CompanyDetails)
admin.site.register(AgentDetails)
admin.site.register(Accreditation)

# Register your models here.
