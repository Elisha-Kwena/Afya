from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm , LoginForm
from django.db.models import Q
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import UserUpdateForm, UserProfileUpdateForm,SearchForm
from clinics.models import Clinic,ClinicServices
from doctors.models import Doctors



# Create your views here.
def home(request):
    return render(request,'home.html')

def registerForm(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save user first
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")

            # Authenticate user
            new_user = authenticate(username=username, password=password)
            if new_user is not None:
                login(request, new_user)
                messages.success(request, "Registration successful! You are now logged in.")
                return redirect("profile")
            else:
                messages.error(request, "User authentication failed after registration.")
        else:
            print(form.errors)  # Debugging: Print form errors
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = SignUpForm()
    
    context = {"form": form}
    return render(request, "register.html", context)

def logout(request):
    auth.logout(request)
    return redirect('home')

def customloginForm(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form .cleaned_data['username']
            password = form .cleaned_data['password']
            
            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request,user)
                if user.is_staff:
                    return redirect('admin_dashboard')
                else:
                    return redirect("home")
            else:
                form.add_error(None, "Invalid username or password")
        
    else:
        form = LoginForm()
        
    context = {
        'form':form
    }
    return render(request,"login.html",context)

# user profile view
@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render (request,"profile.html",{"profile":profile})


@login_required
def update_profile(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)
    
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=user)
        profile_form = UserProfileUpdateForm(request.POST,request.FILES,instance=profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=user)
        profile_form = UserProfileUpdateForm(instance=profile)
        
    context = {
        'user_form':user_form,
        'profile_form':profile_form
    }
    
    return render(request,'update_profile.html',context)

def global_search(request):
    form = SearchForm(request.GET)
    query = request.GET.get('query')
    
    doctors = clinics = clinicServices =[]
    
    if query:
        doctors = Doctors.objects.filter(
            Q(name__icontains=query) | Q(specialization__icontains=query) | Q(location__icontains=query)
            
        )
        clinics = Clinic.objects.filter(
            Q(name__icontains=query) | Q(address__icontains=query)
        )
        clinicServices = ClinicServices.objects.filter(
            Q(name__icontains=query)
        )
        clinics_with_services = Clinic.objects.filter(
            services__in=clinicServices
        )
        
        clinics = list(clinics) + list(clinics_with_services)
    context = {
        'clinics':clinics,
        'doctors':doctors,
        'query':query,
        'clinicServices':clinicServices
    }
    return render(request,"search_results.html",context)