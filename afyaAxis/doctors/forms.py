from django import forms
from .models import Doctors,Appointment

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctors
        fields = ['clinic','name','specialization','phone_number','email','experience','profile_picture','location','distance','about'] 
        
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form_control'}),
            'clinic' : forms.Select(attrs={'class':'select-control'}),
            'specialization' : forms.Select(attrs={'class':'select-control'}),
            'phone_number' : forms.TextInput(attrs={'class':'form_control'}),
            'email' : forms.EmailInput(attrs={'class':'form_control'}),
            'experience' : forms.NumberInput(attrs={'class':'form_control'}),
            'profile_picture' : forms.ClearableFileInput(attrs={'class':'image','id':'profile_picture'}),
            'location' : forms.TextInput(attrs={'class':'form_control'}),
            'distance' : forms.NumberInput(attrs={'class':'form_control'}),
            'about' : forms.TextInput(attrs={'class':'textarea'}),
        }
        
class Appointmentform(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor','appointment_date','time','time','reason','symptoms','location','session_type']
        widgets = {
            'appointment_date': forms.DateInput(attrs={'class':'input','type':'date'}),
            'time': forms.TimeInput(attrs={'class':'input','type':'time'}),
            'reason': forms.Textarea(attrs={'class':'textarea','row':4}),
            'symptoms': forms.Textarea(attrs={'class':'textarea','row':4}),
            'location': forms.TextInput(attrs={'class':'input','type':'text'}),
            'session_type': forms.RadioSelect(choices=Appointment.SESSION_TYPES), 
        }