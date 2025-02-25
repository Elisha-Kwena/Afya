from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import get_user_model
from doctors.models import Doctors,Appointment
from clinics.models import Clinic
from base.models import Profile
from doctors.forms import DoctorForm

User = get_user_model()

def is_admin(user):
    return user.is_authenticated and user.is_staff  

# Create your views here.
@login_required
@user_passes_test(is_admin)
def dashboard(request):
    admin_user = request.user
    admin_profile = Profile.objects.filter(user=admin_user).first()
    users = Profile.objects.select_related('user')
    doctors = Doctors.objects.all()
    clinics = Clinic.objects.all()
    
    appointments_count = Appointment.objects.count()
    doctors_count =Doctors.objects.count()
    
    context = {
        'users':users,
        'doctors':doctors,
        'clinics':clinics,
        'admin_user':admin_user,
        'appointments_count': appointments_count,
        'admin_profile':admin_profile,
        'doctors_count':doctors_count
    }
    return render(request,'admin/admin_dashboard.html',context)

@login_required
@user_passes_test(is_admin)
def clinics(request):
    admin_user = request.user
    admin_profile = Profile.objects.filter(user=admin_user).first()
    users = Profile.objects.select_related('user')
    doctors = Doctors.objects.all()
    clinics = Clinic.objects.all()
    
    context = {
        'users':users,
        'doctors':doctors,
        'clinics':clinics,
        'admin_user':admin_user,
        'admin_profile':admin_profile,
    }
    return render(request,'admin/clinics.html',context)

@login_required
@user_passes_test(is_admin)
def users(request):
    admin_user = request.user
    admin_profile = Profile.objects.filter(user=admin_user).first()
    users = Profile.objects.select_related('user')
    doctors = Doctors.objects.all()
    clinics = Clinic.objects.all()
    
    context = {
        'users':users,
        'doctors':doctors,
        'clinics':clinics,
        'admin_user':admin_user,
        'admin_profile':admin_profile,
    }
    return render(request,'admin/users.html',context)

@login_required
@user_passes_test(is_admin)
def doctors(request):
    admin_user = request.user
    admin_profile = Profile.objects.filter(user=admin_user).first()
    users = Profile.objects.select_related('user')
    doctors = Doctors.objects.all()
    clinics = Clinic.objects.all()
    
    context = {
        'users':users,
        'doctors':doctors,
        'clinics':clinics,
        'admin_user':admin_user,
        'admin_profile':admin_profile,
    }
    return render(request,'admin/doctors.html',context)
@login_required
@user_passes_test(is_admin)
def doctorsprofile(request ,id):
    doctors = Doctors.objects.all()
    admin_user = request.user
    admin_profile = Profile.objects.filter(user=admin_user).first()
    users = Profile.objects.select_related('user')
    doctor = get_object_or_404(Doctors,id=id)
    clinics = Clinic.objects.all()
    
    context = {
        'users':users,
        'doctors':doctors,
        'doctor':doctor,
        'clinics':clinics,
        'admin_user':admin_user,
        'admin_profile':admin_profile,
    }
    return render(request,'admin/docprofile.html',context)

@login_required
@user_passes_test(is_admin)
def doctor_registration(request):
    if request.method == "POST":
        form = DoctorForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('doctorspage')
        else:
            print(form.errors)
    else:
        form = DoctorForm()
    admin_user = request.user
    admin_profile = Profile.objects.filter(user=admin_user).first()
    users = Profile.objects.select_related('user')
    doctors = Doctors.objects.all()
    clinics = Clinic.objects.all()
    
    context = {
        'form':form,
        'users':users,
        'doctors':doctors,
        'clinics':clinics,
        'admin_user':admin_user,
        'admin_profile':admin_profile,
    }
    return render(request,'admin/forms/doctorsform.html',context)