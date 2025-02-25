from django.db import models

# Create your models here.
class ClinicServices(models.Model):
    name = models.CharField(max_length=255,unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='clinics_images',null =True,blank=True)
    
    def __str__(self):
        return self.name
    

class Clinic(models.Model):
    name = models.CharField(max_length=255,unique=True)
    address =models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True,null=True,blank = True)
    services = models.ManyToManyField(ClinicServices, related_name='clinics')
    opening_hours = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='clinics_images',null =True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name