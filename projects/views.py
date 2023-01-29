from django.shortcuts import render, redirect
from .models import Project
import datetime
from accounts.models import Profile as User
# Create your views here.
def index(request):
    jobs = Project.objects.all().order_by('-date_created')
    return render(request, 'jobs-reading-page.html',{'jobs':jobs})
def create_job_page(request):
    return render(request, 'create.html')
def create_project(request):
    project = Project()
    project.name = request.POST['name']
    project.description = request.POST['description']
    project.details = request.POST['details']
    project.pay = request.POST['payment']
    project.creator = User.objects.get(username=request.user.username)
    project.save()
    return redirect(jobs_created_by_user)
def jobs_created_by_user(request):
    projects_created_by_user = Project.objects.filter(creator=User.objects.get(username=request.user.username)).order_by('is_it_done')
    return render(request, 'profile-created-jobs.html', {'user_jobs':projects_created_by_user} )