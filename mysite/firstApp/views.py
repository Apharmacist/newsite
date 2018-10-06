from django.shortcuts import render

# Create your views here.
from .models import Projects, Peoples

def index(request):
    return render(request, 'fistApp/index.html')




def projects(request):
    projectList = Projects.objects.all()
    text = {'students': projectList}
    return render(request, 'firstApp/students.html', text)

def peoples(request):
    peopleList = Peoples.objects.all()
    text2 = {'students': peopleList}
    return render(request, 'myApp/students.html', text2)