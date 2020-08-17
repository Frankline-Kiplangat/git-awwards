# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm,UploadForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form':form})



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
def upload_form(request):
    current_user = request.user.profile
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.uploaded_by = current_user
            image.save()
            messages.success(request, f'You have uploaded the project!')
            return redirect('index')
    else:
        form = UploadForm()
    return render(request, 'post_project.html', {'uploadform': form})


@login_required(login_url='login')
def project(request, project_id):
    """
    Function that returns project details
    """
    try:
        project = Projects.objects.get(id=project_id)
    except Projects.DoesNotExist:
        raise Http404()
    return render(request, "project.html", {'project':project})

@login_required(login_url='login')
def index(request):
    """
    view function renders the landing page
    """
    current_user = request.user
    all_projects = Projects.objects.all()
    return render(request, 'index.html', {'all_projects':all_projects})

@login_required(login_url='login')
def profile(request):
    """
    view function that renders user's profile
    """
    current_user = request.user
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save() 
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        my_projects = Projects.objects.filter(project_user=current_user)
        
    
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'my_projects':my_projects    
    }
    return render(request, 'profile.html', context)
