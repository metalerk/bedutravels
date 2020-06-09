from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from rest_framework import viewsets
from tours.models import User as tours_user
from profiles.serializers import TourUserSerializer
from utils import list2str

@login_required()
def user_profile(request):
    user_qs = User.objects.get(pk=request.user.pk)
    return render(
        request,
        'profiles/profile.html',
        {
            'user': user_qs,
        }
    )

@login_required()
def save_profile(request):
    if request.method == 'POST':
        form = {k: list2str(v) for k, v in request.POST.items()}
        form.pop('csrfmiddlewaretoken', None)
        form.pop('button', None)
        #tours_user.objects.create(**form)
        print(form)
    
    return redirect(reverse('profile:index'))

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


class UserViewSet(viewsets.ModelViewSet):
    queryset = tours_user.objects.all().order_by('id')
    serializer_class = TourUserSerializer