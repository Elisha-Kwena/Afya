from django.shortcuts import render

# Create your views here
def maternalHealth(request):
    return render(request,'health/maternal_health.html')
def diseases(request):
    return render(request,'health/diseases.html')
def healthconcerns(request):
    return render(request,'health/health_concerns.html')
