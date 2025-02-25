from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    GENDER_CHOICES = [
        ("Male","Male"),
        ("Female","Female"),
        ("Prefer Not to Say","Prefer Not to Say"),
    ]    
    
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    sex = models.CharField(max_length=20, choices = GENDER_CHOICES, blank=True,null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='default.png', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"





