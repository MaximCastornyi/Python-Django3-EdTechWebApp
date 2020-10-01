from django.urls import path
from . import views

urlpatterns = [
     path('',views.home, name='home'),
     path('Being-a-Rainmaker-During-COVID-19/',views.aboutus, name='about'),

]
