from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns =[
    path('clinics/',views.clinicPage,name='clinics'),
    path('new_clinics',views.new_clinic,name='new_clinics'),
    path('clinicDetails/<int:id>/',views.clinic_details,name='clinicDetails')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)