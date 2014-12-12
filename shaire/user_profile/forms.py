# -*- coding: utf-8 -*-
from loginsys.models import Users
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailInput, TextInput, PasswordInput, DateInput, FileInput, Select
from django.forms.extras.widgets import SelectDateWidget

class ChangeAvatar(forms.ModelForm):
	class Meta:
		model = Users
		fields = ('user_photo',)


class ChangeName(forms.ModelForm):
	class Meta:
		model = Users
		fields = ('user_firstname',)
		widgets = {
			'user_firstname': TextInput(attrs={'placeholder': 'Имя', 'class': 'form-control'}),
		}


class ChangeSecondName(forms.ModelForm):
	class Meta:
		model = Users
		fields = ('user_surname',)
		widgets = {
			'user_surname': TextInput(attrs={'placeholder': 'Фамилия', 'class': 'form-control'}),
		}


class ChangeCity(forms.ModelForm):
	class Meta:
		model = Users
		fields = ('user_city',)
		widgets = {
			'user_city': TextInput(attrs={'placeholder': 'Город', 'class': 'form-control'}),
		}


class ChangeBirthday(forms.ModelForm):
	class Meta:
		model = Users
		fields = ('user_birthday',)
		widgets = {
			'user_birthday': SelectDateWidget(years=range(2014, 2014-100, -1), attrs={'placeholder': 'Возраст', 'class': 'btn-data'}),
		}


class ChangeSex(forms.ModelForm):
	class Meta:
		model = Users
		fields = ('user_sex',)
		widgets = {
			'user_sex': Select(choices=(('М', 'Мужской',), ('Ж', 'Женский',)), attrs={'placeholder': 'Пол', 'class': 'form-control'})
		}


class ChangeVK(forms.ModelForm):
	class Meta:
		model = Users
		fields = ('user_vk',)
		widgets = {
			'user_vk': TextInput(attrs={'placeholder': 'VK ID', 'class': 'form-control'}),
		}




