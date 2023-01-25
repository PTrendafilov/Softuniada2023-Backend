from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'jobs-reading-page.html')
def create_job_page(request):
    return render(request, 'create.html')