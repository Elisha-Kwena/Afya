from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('admin_dashboard/',views.dashboard,name="admin_dashboard"),
    path('adminclinics/',views.clinics,name="adminclinics"),
    path('users/',views.users,name="users"),
    path('docprofile/<int:id>/',views.doctorsprofile,name="docprofile"),
    path('doctorspage/',views.doctors,name="doctorspage"),
    path('doctor_form/',views.doctor_registration,name='doctor_form')
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
