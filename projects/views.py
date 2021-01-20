from django.shortcuts import render
# import the model to be able to use the data
from .models import Project

# Create your views here.
def home(request):
    # get all project data
    projects = Project.objects.all()[:4]
    # render the template
    return render(request,'projects/home.html',{'projects':projects})
