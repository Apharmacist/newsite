from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from .models import Students, Grades
def students(request):
    studentList = Students.stuObj.all()
    text = {'students': studentList}
    return render(request, 'myApp/students.html', text)



def students3(request):
    studentList = Students.stuObj.all()[0: 5]
    text = {'students': studentList}
    return render(request, 'myApp/students.html', text)


# 分页显示学生
def stupage(request, num):
    num = int(num)
    studentList = Students.stuObj.all()[(num - 1) * 5:num * 5]
    text3 = {'students':studentList}
    return render(request, 'myApp/students.html', text3)





def grades (request):
    gradesList = Grades.objects.all()
    text1 ={'grades': gradesList}
    return render(request, 'myApp/grades.html', text1)

def gradeStudent(request, num_id):
    grade = Grades.objects.get(pk=num_id)
    gradeList = grade.students_set.all()
    text2 = {'students': gradeList}
    return render(request, 'myApp/students.html', text2)

def addStudent(request):
    grade1 = Grades.objects.get(pk=1)
    stu = Students.createStudent("zhoujiwe", 34, True, 'wojiaozhoujie', grade1, False)
    stu.save()
    return HttpResponse("123")

def addStudent2(request):
    grade1 = Grades.objects.get(pk=1)
    stu = Students.createStudent("zhoujiwe2", 34, True, 'wojiaozhoujie2', grade1, False)
    stu.save()
    return HttpResponse("####")


from django.db.models import Max, Min, F, Q
def studentSearch(request):
    # studentsList = Students.stuObj.filter(s_name__contains="li")
    # studentsList = Students.stuObj.filter(s_name__startswith="li")
    # studentsList = Students.stuObj.filter(pk__in=[2, 4, 6, 8, 10])
    # studentsList = Students.stuObj.filter(lastTime__year=2017)
    # studentsList = Students.stuObj.filter(s_age__gt=20)
    # studentsList = Students.stuObj.filter(s_name__contains='li%')
    # 描述带有“lilei”两个字的数据属于哪个班级
    gradesList = Grades.objects.filter(grades__s_name__contains='lilei')

    # studentsList = Students.stuObj.filter(lastTime__year=2017)
    #studentsList = Students.stuObj.filter(Q(pk__lte=6) | Q(s_age__gt=50))

    text5 = {'students': gradesList}
    print(gradesList)

    # maxAge = Students.stuObj.aggregate(Max('s_age'))
    # print(maxAge)

    return render(request, 'myApp/students.html', text5)




def grade2 (request):
    # g = Grades.objects.filter(g_girl_num__gt=F('g_boy_num'))
    # print(g)

    return HttpResponse('############')