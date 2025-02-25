from django.shortcuts import render,redirect,get_object_or_404
from .forms import DoctorForm,Appointmentform
from .models import Doctors,Appointment

# Create your views here.
def register_doctor(request):
    if request.method == "POST":
        form = DoctorForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('doctors_list') 
        else:
            print(form.errors)
    else:
        form = DoctorForm()
    return render(request, 'doctors/register_doc.html', {'form': form})

def doctorsList(request):
    doctors = Doctors.objects.all()
    context = {
        'doctors':doctors
    }
    return render(request, 'doctors/doctors_list.html',context)       

def doctor_details(request,id):
    doctor = get_object_or_404(Doctors,id=id)
    context = {
        'doctor':doctor
    }
    return render (request,'doctors/doctor_profile.html',context)

def book_appointment(request,id):
    doctor = get_object_or_404(Doctors, id=id)
    
    if request.method == "POST":
        form = Appointmentform(request.POST)
        if form.is_valid():
            appointment = form.save(commit = False)
            appointment.patient = request.user
            appointment.doctor = doctor
            appointment.save()
            return redirect('appointment_success')
    else:
        form = Appointmentform(initial = {'doctor':doctor,'patient':request.user})
    context = {
        'doctor':doctor,
        'form':form
    }
    return render(request,'doctors/book_appointment.html',context)
            
def appointmentSuccess(request):
    return render(request,'doctors/appointment_success.html') 
    
    