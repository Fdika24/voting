from django import forms
from django.core import validators
from django.contrib.auth.models import User
from voting_system.models import Userdata,Fakultas
# Todo List : Perbaikin drop down system

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }
        fields = ('username', 'email', 'password')


class UserFakultas(forms.ModelForm):

    class Meta:
        model = Userdata
        fields =['faculty']

        def __init__(self,*args,**kwargs):
            super().__init__(*args, **kwargs)
            choices = [(faculty.id, faculty) for faculty in Fakultas.objects.all()]
            self.fields['faculty'] = forms.ChoiceField(widget=forms.Select(attrs={'class': 'select2-single form-control','id':"select2Single"}), choices=choices)




