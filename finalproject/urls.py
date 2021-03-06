"""finalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from student import views
from coursedetails import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('login/', LoginView.as_view(template_name='student/login.html'), name='login'),
    path('admin/', admin.site.urls),
    path('home/', views.home, name='dashboard'),
    path('studentdetails/', views.studentdetails, name='studentdetails'),
    path('coursedetails/', views.coursedetails, name='coursedetails'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('enrollment/', views.enrollment, name='enrollment'),
    path('saveenrollment/',views.saveenrollment, name='saveenrollment')
]
