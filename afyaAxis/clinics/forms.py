from django import forms
from .models import Clinic,ClinicServices

class NewClinic(forms.ModelForm):
    services = forms.ModelMultipleChoiceField(
        queryset=ClinicServices.objects.all(),  # Fetch all services
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form_control'}),
        required=True
    )
    class Meta:
        model = Clinic
        fields = ['name','address','email','phone_number','opening_hours','description','image','services']
        
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form_control'}),
            'address' : forms.Textarea(attrs={'class':'form_control','rows': 3,'placeholder':'123 Mwembe, Kisii'}),
            'email': forms.EmailInput(attrs={'class':'form_control'}),
            'phone_number' : forms.TextInput(attrs={'class':'form_control'}),
            'opening_hours' : forms.TimeInput(attrs={'class':'form_control','type':'time'}),
            'description' : forms.Textarea(attrs={'class':'form_control'}),
            'image' : forms.ClearableFileInput(attrs={'class':'form_control','id':'image'}),
             
        }
        