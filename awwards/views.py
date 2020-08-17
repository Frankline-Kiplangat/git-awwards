# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm,UploadForm

# Create your views here.
def search_results(request):
    """
    view function that returns the searched projects
    """
    if 'projects' in request.GET and request.GET["projects"]:
        project_search = request.GET.get("projects")
        searched_projects = Projects.get_projects(project_search)
        message = f"{project_search}"

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any user or projects"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='login')
def project(request, project_id):
    try:
        project = Projects.objects.get(id=project_id)
    except Projects.DoesNotExist:
        raise Http404()
    return render(request, "project.html", {'project':project})
