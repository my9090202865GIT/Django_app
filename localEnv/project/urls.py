"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include

import movieapp
from firstapp.views import first_page, hyd_jobs, bang_jobs, pune_jobs
from modelformapp.views import student_view
from movieapp.views import index_view
from testapp.views import studentinput_view, feedback_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', first_page),
    path('hyd/', hyd_jobs),
    path('bang/', bang_jobs),
    path('pune/', pune_jobs),
    path('form/', studentinput_view),
    path('feedback/', feedback_view),
    path('std/', student_view),
    path('movie/', include("movieapp.urls"))
]
