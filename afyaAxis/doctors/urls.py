from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns =[
    path('register-doctor/', views.register_doctor, name='register_doctor'), 
    path('doctors_list/',views.doctorsList,name='doctors_list'),
    path('appointment_success/',views.appointmentSuccess,name='appointment_success'),
    path('doctor/<int:id>/',views.doctor_details,name ="doctor_detail"),
    path('book_appointment/<int:id>/',views.book_appointment,name='book_appointment'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
