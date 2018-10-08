from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('peoples/', views.peoples, name='peoples'),
    path('attribles/', views.attribles, name='attribles'),
    path('get1', views.get1, name='get1'),
    path('get2', views.get2, name='get2'),
    path('showregis/', views.showregis),
    path('showregis/register/', views.register, name='register'),
    path('showresponse/', views.showresponse, name='showresponse'),
    path('cookietest/', views.cookietest, name='cookietest'),
    path('redirect1/', views.redirect1, name='redirect1'),
    path('redirect2', views.redirect2, name='redirect2'),
    path('main/', views.main, name='main'),
    path('login/', views.login, name='login'),
    path('showmain/', views.showmain, name='showmain'),
    path('quit/', views.quit, name='quit'),
]