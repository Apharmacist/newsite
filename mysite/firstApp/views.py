from django.shortcuts import render, redirect
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

    return HttpResponse(a1+ "" + a2 + "" + c)




# POST

def showregis(request):
    return render(request, 'firstApp/register.html')



def register(request):
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    age = request.POST.get('age')
    hobby = request.POST.get('hobby')
    print(name)
    print(gender)
    print(age)
    print(hobby)
    return HttpResponse('post')


# response
def showresponse(request):
    res = HttpResponse()
    res.content = b'good'
    print(res.content)
    print(res.charset)
    print(res.status_code)


    return res


# cookie

def cookietest(request):
    res = HttpResponse()
    cookie = request.COOKIES
    res.write('<h1>' + cookie['firstApp']+'<h1/>')
    # cookie = res.set_cookie('firstApp', 'good')
    return res



# 重定向
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect

def redirect1(request):
   # return HttpResponseRedirect('/firstApp /redirect2')
    return redirect('/firstApp/redirect2')

def redirect2(request):

   # if request.is_ajax():
   #     a = JsonResponse({})

    return HttpResponse('我是重定向后的视图')




# session

def main(request):

    # 取session
    username = request.session.get('name', "游客                                 ")
    return render(request, 'firstApp/main.html', {'username': username})


def login(request):
    return render(request, 'firstApp/login.html')


def showmain(request):
    username = request.POST.get('username')


    # 存储session
    request.session['name'] = username
    # request.session.set_expiry(10)
    return redirect('/firstApp/main')

from django.contrib.auth import logout
def quit(request):
    # 清除session

    logout(request)
    return redirect('/firstApp/main')