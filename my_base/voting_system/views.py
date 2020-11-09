from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.models import User
from voting_system.forms import UserForm, UserFakultas

from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(response):
    total = User.objects.count()
    return render(response, 'Main/index.html',{'total':total})

@ login_required
def voting(response):
    return render(response, 'Main/blank.html')  # balik ke sendiri


def token(response):
    return 0  # balik ke sendiri

@ login_required
def user_logout(response):
    logout(response)
    return HttpResponseRedirect(reverse('voting_system:login'))


def user_login(response):
    if response.user.is_authenticated:
        return HttpResponseRedirect(reverse('voting_system:index'))
    if response.method == 'POST':
        username = response.POST.get('username')
        password = response.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(response,user)
                return HttpResponseRedirect(reverse('voting_system:index'))
            else: return HttpResponse("Account not active")
        else:
            print('Someone failed')
            return HttpResponse('Failed ')

    return render(response, 'Main/login.html',{})


def register(response):
    user_form = UserForm()
    profile_form = UserFakultas()
    if response.method == 'POST':
        user_form = UserForm(data=response.POST)
        profile_form = UserFakultas(data=response.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

        else:
            print(user_form.errors, profile_form.errors)
    return render(response, 'Main/register.html', {
        'form': user_form, 'form2': profile_form
    })


def handler404(res,*args,**kwargs):
    return render(res, 'Main/404.html', status=404)
