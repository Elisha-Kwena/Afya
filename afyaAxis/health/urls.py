from django.urls import path
from . import views
urlpatterns = [
    path('maternal/',views.maternalHealth,name="maternal"),
    path('diseases/',views.diseases,name="diseases"),
    path('healthconcerns/',views.healthconcerns,name="healthconcerns")
]
