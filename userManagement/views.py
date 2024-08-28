from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.mail import send_mail

from userManagement.forms import UserCreateForm, DepartmentForm, HeaderSettingsForm
from userManagement.models import Department, RegistrationRequest, HeaderSettings, PasswordResetRequest
from surveys.models import Defaults



def index(request):
    return redirect('https://www.schoolleader360.com/')

def register(request):
        if request.POST:
                creation_form = UserCreateForm(request.POST)
                if request.POST.get('rid') and RegistrationRequest.objects.filter(rid=request.POST.get('rid')).exists():
                        if creation_form.is_valid():
                                creation_form.save()
                                username = creation_form.cleaned_data['username']
                                password = creation_form.cleaned_data['password1']

                                user = authenticate(username=username, password=password)
                                Defaults.objects.create(user=user)
                                login(request, user)
                                RegistrationRequest.objects.filter(rid=request.POST.get('rid')).delete()
                                return redirect('surveys/')
                else:
                        return HttpResponse('Access Denied')
                
        creation_form = UserCreateForm()
        context = {
                'form': creation_form,
                'rid': request.GET.get('rid', )
                }   

        return render(request, 'registration/register.html', context)

def user_profile(request):
        return render(request, 'userManagement/user_profile.html')


def add_department(request):
        if request.POST:
                form = DepartmentForm(request.POST)

                if form.is_valid():
                        department = form.save()
                        department.users.add(request.user)
                        return redirect('department-profile', department.id)

        initial = {'admin': request.user}
        form = DepartmentForm(initial=initial)
        context = {'form': form}
        return render(request, 'userManagement/add_department.html', context)

def department_profile(request, id):
        department = Department.objects.filter(id=id).first()
        context = {'department': department}

        return  render(request, 'userManagement/department_profile.html', context)

def subscribers(request):
        users = User.objects.filter(is_superuser=False)
        if not request.user.is_superuser:
                return HttpResponse('Access Denied')
        return render(request, 'userManagement/subscribers.html', {'users': users})

def edit_survey_header(request):
        if HeaderSettings.objects.filter(user=request.user).exists():
                settings = HeaderSettings.objects.filter(user=request.user).first()
        else:
                settings = HeaderSettings.objects.create(user=request.user)
        
        form = HeaderSettingsForm(instance=settings)

        if request.POST:
                form = HeaderSettingsForm(request.POST, request.FILES, instance=settings)

                if form.is_valid():
                        form.save()
                        return redirect('user-profile')
        
        context = {
                'settings': settings,
                'form': form
        }
        return render(request, 'userManagement/edit_survey_header.html', context)

def forgot_password(request):
        if request.POST:
                email = request.POST.get('email')
                user = User.objects.filter(email=email)

                if user.exists():
                        user = user.first()
                        req = PasswordResetRequest.objects.create(user=user)

                        survey_url = request.get_host()+reverse('reset-password')+'?key='+str(req.rid)
                        message = 'A password reset link for your account at schoolleader360 was requested. follow this link to reset your password '+survey_url
                        send_mail(
                        'Password Reset',
                        message,
                        'automated@schoolleader360.com',
                        [email],
                        fail_silently=False,
                        )
                
                return render(request, 'userManagement/forgot_password.html', {'confirmation': True})


        return render(request, 'userManagement/forgot_password.html')

def reset_password(request):
        if request.GET.get('key'):
                req = PasswordResetRequest.objects.filter(rid=request.GET.get('key'))

                if req.exists():
                        req = req.first()
                        if request.POST:
                                password = request.POST.get('password')
                                user = req.user

                                user.set_password(password)
                                user.save()
                                req.delete()
                                return render(request, 'userManagement/reset_password.html', {'confirmation': True})
                        return render(request, 'userManagement/reset_password.html')
        return HttpResponse('No Key Found')
