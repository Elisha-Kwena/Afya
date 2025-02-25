from django.db import models
from django.contrib.auth.models import User
from clinics.models import Clinic


# Create your models here.
class Doctors(models.Model):
    
    SPECIALIZATIONS =[
        ('Cardiologist','Cardiologist'),
        ('Darmatologist','Darmatologist'),
        ('Neurologist','Neurologist'),
        ('Pediatrician','Pediatrician'),
        ('Orthopedic','Orthopedic'),
        ('General Practitioner','General Practitioner'),
    
    ]
    
    name = models.CharField(max_length=250)
    specialization = models.CharField(max_length=255, choices = SPECIALIZATIONS)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name="doctors")
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=255)
    about = models.TextField()
    profile_picture =models.ImageField(upload_to='profile_pics/',blank=True,null=True,default='profile_pics/logo.png')
    experience = models.IntegerField(help_text="Years of experience")
    distance = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Dr. {self.name} - {self.specialization}"
    
class Appointment(models.Model):
    SESSION_TYPES =[
        ('video','video call'),
        ('audio','audio call')
    ]
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    location =models.TextField()
    appointment_date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()
    symptoms = models.TextField()
    session_type = models.CharField(max_length=10,choices=SESSION_TYPES,default='video')
    
    def __str__(self):
        return f"Appointment with {self.doctor.name} on {self.appointment_date} at {self.time}"