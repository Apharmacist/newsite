from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Projects, Peoples

def index(request):
    return render(request, 'firstApp/index.html')




def projects(request):
    projectList = Projects.objects.all()
    text = {'students': projectList}
    return render(request, 'firstApp/projects.html', text)

def peoples(request):
    peopleList = Peoples.objects.all()
    text2 = {'students': peopleList}
    return render(request, 'firstApp/peoples.html', text2)



def attribles(request):
    print(request.path)
    print(request.method)
    print(request.encoding)
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.SESSION)

    return HttpResponse('TOM is a good boy')


# 获取get传递的数据

def get1(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')

    return HttpResponse(a + "" + b + "" + c)


def get2(request):
    a = request.GET.getlist('a')
    a1 = a[0]
    a2 = a[1]
    c = request.GET.get('c')

    return HttpResponse(a1+ "" + a2 +""+ c)