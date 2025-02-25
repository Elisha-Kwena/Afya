from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views

urlpatterns =[
    path('',views.home,name='home'),
    path('register/',views.registerForm,name='register'),
    path("logout/",views.logout,name='logout'),
    path("login/",views.customloginForm,name='login'),
    path("profile/",views.profile,name='profile'),
    path('profile/update/',views.update_profile, name='update_profile'),
    path('search/',views.global_search, name='global_search'),
    
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
