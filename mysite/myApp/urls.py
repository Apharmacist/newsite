from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='index'),
    path('students/', views.students, name='students'),
    path('students3/', views.students3, name='students3'),

    path('stu/<int:num>/', views.stupage, name='stupage'),


    path('grades/', views.grades, name='grades'),
    path('grades/<int:num_id>/', views.gradeStudent, name='gradeStudent'),
    path('addStudent/', views.addStudent, name='addStudent'),
    path('addStudent2/', views.addStudent2, name='addStudent2'),

    path('studentSearch/', views.studentSearch, name='studentSearch'),
    path('grade2/', views.grade2, name='grade2'),

]