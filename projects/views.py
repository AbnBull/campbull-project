from django.shortcuts import render

from .models import Project

def home(request):
    return render(request, 'projects/home.html' )

def projectsmain(request):
    projects = Project.objects
    return render(request, 'projects/projectsmain.html', {'projects':projects})

def project_detail(request):
    return render(request, 'projects/project_detail.html' )
