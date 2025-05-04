from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('createblog/', views.createblog, name = 'createblog'),
    path('readblog/<int:id>/', views.readblog, name = 'readblog'), 
    path('editblog/<int:id>/', views.editblog, name = 'editblog'),
    path('deleteblog/<int:id>/', views.deleteblog, name = 'deleteblog')
]