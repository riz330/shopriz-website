from operator import index
from django.contrib import admin
from django.urls import path
from home import views
import home

urlpatterns = [
    
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("services",views.service,name='services'),
    path("contact",views.contact,name='contact')
]
