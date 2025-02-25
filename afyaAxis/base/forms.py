from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'required':'',
            'name':'username',
            'id':'username',
            'type':'text',
            'class':'input',
            'maxlength':'16',
            'minlength':'6'
        })
        self.fields["email"].widget.attrs.update({
            'required':'',
            'name':'email',
            'id':'email',
            'type':'text',
            'class':'input',
            'maxlength':'40',
            'minlength':'10'
        })
        self.fields["password1"].widget.attrs.update({
            'required':'',
            'name':'password1',
            'id':'password1',
            'type':'password',
            'class':'input',
            'minlength':'8'
        })
        self.fields["password2"].widget.attrs.update({
            'required':'',
            'name':'password2',
            'id':'password2',
            'type':'password',
            'class':'input',
            'minlength':'8'
        })
        
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'required':'',
            'name':'username',
            'id':'username',
            'type':'text',
            'class':'input',
        })
    )
    password = forms.CharField(
        widget=forms.TextInput(attrs={
            'required':'',
            'name':'password',
            'id':'password',
            'type':'password',
            'class':'input',
        })
    )
    
    
class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=255, required=False)
    last_name = forms.CharField(max_length=255, required=False)
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        
        widgets = {
            'username': forms.TextInput(attrs={'class':'inputcontbox'}),
            'first_name' : forms.TextInput(attrs={'class':'inputcontbox'}),
            'last_name' : forms.TextInput(attrs={'class':'inputcontbox'}),
            'email' : forms.EmailInput(attrs={'class':'inputcontbox'}),
        }
        
class UserProfileUpdateForm(forms.ModelForm):
    profile_picture = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}))
    class Meta:
        model = Profile
        fields = ['profile_picture','phone_number','location','about','sex']
        
        widgets = {
            'sex' : forms.Select(attrs={'class':'select-control'}),
            'phone_number' : forms.TextInput(attrs={'class':'inputcontbox'}),
            'profile_picture' : forms.ClearableFileInput(attrs={'class':'image','id':'profile_picture'}),
            'location' : forms.TextInput(attrs={'class':'inputcontbox'}),
            'about' : forms.Textarea(attrs={'class':'textarea'}),
        }
        
        
class SearchForm(forms.Form):
    query = forms.CharField(max_length=255,required=False)