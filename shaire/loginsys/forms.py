# -*- coding: utf-8 -*-
from loginsys.models import Users
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailInput, TextInput, PasswordInput, DateInput, FileInput, Select
from django.forms.extras.widgets import SelectDateWidget
from captcha.fields import ReCaptchaField


class MyRegistrationForm(forms.ModelForm):
	captcha = ReCaptchaField(attrs={'theme' : 'red'})
	class Meta:
		model = Users
		fields = ('user_photo', 'user_firstname', 'user_surname', 'user_city', 'user_birthday', 'user_sex', 'user_vk',)
		widgets = {
			'user_firstname': TextInput(attrs={'class': 'form-control'}),
			'user_surname': TextInput(attrs={'class': 'form-control'}),
			'user_city': TextInput(attrs={'class': 'form-control'}),
			'user_vk': TextInput(attrs={'class': 'form-control'}),
			'user_birthday': SelectDateWidget(years=range(2014, 2014-100, -1), attrs={'class': 'btn-data'}),
			'user_photo': FileInput(),
			'user_sex': Select(choices=(('М', 'Мужской',), ('Ж', 'Женский',)), attrs={'class': 'form-control'})
		}

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	class Meta:
		model = User
		fields = ('username', 'email', 'password')
		widgets = {
			'username': TextInput(attrs={'class': 'form-control'}),
			'email': EmailInput(attrs={'class': 'form-control'}),
			#'password': PasswordInput(attrs={'placeholder': 'Пароль'}),
		}