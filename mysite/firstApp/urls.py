from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('peoples/', views.peoples, name='peoples'),
    path('attribles/', views.attribles, name='attribles'),
    path('get1', views.get1, name='get1'),
    path('get2', views.get2, name='get2'),
]