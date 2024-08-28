from django.urls import path
from django.conf.urls import url

from . import views, api

urlpatterns = [
    path('', views.index, name='index'),
    path('forgot-password', views.forgot_password, name='forgot-password'),
    path('reset-password', views.reset_password, name='reset-password'),
    path('register', views.register, name='register'),
    path('user-profile', views.user_profile, name='user-profile'),
    path('add-department', views.add_department, name='add-department'),
    path('subscribers', views.subscribers, name='subscribers'),
    path('edit-survey-header', views.edit_survey_header, name='edit-survey-header'),
    path('delete-user', api.delete_user, name='delete-user'),
    path('registration-link', api.registration_link, name='registration-link'),
    url(r'^department/(?P<id>[0-9a-zA-Z\-_]+)/$', views.department_profile, name='department-profile'),
]