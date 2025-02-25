from django.contrib import admin
from .models import Clinic,ClinicServices

# Register your models here.
admin.site.register(Clinic)
admin.site.register(ClinicServices)
