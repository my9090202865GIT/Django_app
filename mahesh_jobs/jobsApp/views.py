from django.http import HttpResponse
from django.shortcuts import render
from jobsApp.models import HydJobs, PuneJobs, BangJobs


# Create your views here.
def home_view(request):
    return HttpResponse('<h1>Home page</h1>')


# Create your views here.
def first_page(request):
    # For Fronted checking--- start
    if request.method == 'GET':
        for k, v in request.GET.items():
            print(f'{k}-->{v}')
        print(request.GET)  # <QueryDict: {'name': ['Amiya']}>
    # Fronted checking -- end
    return render(request, 'firstapp/index.html')


def hyd_jobs(request):
    hyd_jobs = HydJobs.objects.all()
    my_dict = {'hyd_jobs': hyd_jobs}
    return render(request, 'firstapp/hydjobs.html', my_dict)


def pune_jobs(request):
    pune_jobs = PuneJobs.objects.all()
    my_dict = {'pune_jobs': pune_jobs}
    return render(request, 'firstapp/punejobs.html', my_dict)


def bang_jobs(request):
    bang_jobs = BangJobs.objects.all()
    my_dict = {'bang_jobs': bang_jobs}
    return render(request, 'firstapp/bangjobs.html', my_dict)
