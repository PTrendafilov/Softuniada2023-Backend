from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from accounts.models import Profile as User
# Create your views here.
from django.http import HttpResponse
import os
def index(request,username):
    user=User.objects.get(username=username)
    cv = CV.objects.get(user=user)
    cv.skills = cv.skills.split('(*)')
    context = {'user': user, 'cv': cv}
    return render(request, 'profile-details-page.html', context)

def create_page(request):
    user = request.user
    print(CV.objects.filter(user=user).exists())
    # Check if the user has already created a CV
    if CV.objects.filter(user=user).exists():
        return redirect('index', username=user.username)
    return render(request, 'create-profile-details.html')

def create_cv(request):
    user = request.user
    cv = CV(user=user,
            title=request.POST['title'],
            about_me=request.POST['about-me'],
            skills=request.POST['skills'],
            file=request.FILES['CV-file'])
    cv.save()
    return redirect('index', username=user.username)

def download_cv(request, username):
    user=User.objects.get(username=username)
    cv = CV.objects.get(user=user)
    filepath = cv.file.path
    if os.path.exists(filepath):
        with open(filepath, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(filepath)}"'
            return response
        
def profile_edit_page(request, username):
    user = get_object_or_404(User, username=username)
    cv = get_object_or_404(CV, user=user)
    cv.skills = cv.skills.split('(*)')
    context = {'user': user, 'cv': cv}
    return render(request, 'profile-edit-page.html', context)

def profile_edit(request, username):
    user = get_object_or_404(User, username=username)
    cv = get_object_or_404(CV, user=user)
    if request.method == 'POST':
        cv.title = request.POST.get('title', cv.title)
        cv.about_me = request.POST.get('about-me', cv.about_me)
        cv.skills = request.POST.get('skills', cv.skills)
        if request.FILES.get('CV-file', False):
            cv.file = request.FILES['CV-file']
        cv.save()
        return redirect('index', username=username)
    context = {'user': user, 'cv': cv}
    return redirect('profile_edit_page', username=username)

def profile_delete(request, username):
    user = get_object_or_404(User, username=username)
    cv = get_object_or_404(CV, user=user)
    cv.delete()
    context = {'user': user, 'cv': cv}
    return redirect(create_page)