from django.urls import path
from . import views
urlpatterns=[
    path('home1/',views.index1,name='index1'),
    path('home2/',views.index2,name='index2'),
    path('signin/',views.index3,name='index3'),
    path('signup/',views.SignupForm,name='SignupForm'),
    path('thank/',views.index5,name='index5'),
    path('about/',views.index6,name='index6'),
    ]