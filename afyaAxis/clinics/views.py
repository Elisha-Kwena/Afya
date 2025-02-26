from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Clinic,ClinicServices
from .forms import NewClinic

# Create your views here.
def clinicPage(request):
    clinics = Clinic.objects.all()
    context = {
        'clinics':clinics
    }
    return render(request,'clinics/clinics.html',context)

@login_required
def new_clinic(request):
    if request.method == "POST":
        print(request.POST) 
        form = NewClinic(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("Clinic saved!") 
            return redirect('clinics') 
        else:
            print(form.errors) 
    else:
        form = NewClinic()
    
    return render(request, 'clinics/new_clinic.html', {'form': form})

@login_required
def clinic_details(request,id):
    clinic = get_object_or_404(Clinic,id=id)
    clinic_services = clinic.services.all()  
    context = {
        'clinic':clinic,
        'clinic_services':clinic_services
    }
    return render(request,'clinics/clinic_details.html',context)