from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Tour

@login_required()
def index(request):
    tours = Tour.objects.all()
    return render(
        request,
        'tours/index.html',
        {
            'tours': tours,
            'tour_arrivals': tours.distinct().values_list('arrival_zone__name', flat=True),
            'tour_takeoff': tours.distinct().values_list('takeoff_zone__name', flat=True),
            'user': request.user,
        }
    )

def login_user(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        _next = request.GET.get('next', '/')
        access = authenticate(username=username, password=password)
        if access is not None:
            login(request, access)
            return redirect(_next)
        else:
            msg = 'Bad credentials!'
    else:
        msg = ''
    
    return render(
        request,
        'registration/login.html',
        {
            'msg': msg,
        }
    )

def logout_user(request):
    _next = request.GET.get('next', '/')
    logout(request)
    return redirect(_next)