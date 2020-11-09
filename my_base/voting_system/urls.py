from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from voting_system import views as voting

app_name = 'voting_system'
handler404 = voting.handler404
urlpatterns = [
    path('',voting.index, name='index'),
    path('register/', voting.register, name ='register'),
    path('login/', voting.user_login, name='login'),
    path('vote/', voting.voting, name='voting'),
    # path('404/', voting.handler404, name='404'),
    path('logout', voting.user_logout, name ='logout'),
]