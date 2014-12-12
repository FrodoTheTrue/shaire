# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.core.context_processors import csrf
from loginsys.forms import MyRegistrationForm, UserForm
from loginsys.models import Users
from django.contrib.auth.models import User
from django.core.mail import send_mail
import random
from captcha.fields import ReCaptchaField

# Create your views here.

def login(request):
	if request.user.is_authenticated():
		return redirect('/')
	args = {}
	args.update(csrf(request))
	if request.POST:# and ("pause" not in request.session):
	#	request.session.set_expiry(5)
	#	request.session['pause'] = True
		username = request.POST['username']
		password = request.POST['password']
		print(username, password)
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('/profile/' + str(username))
		else:
			args['login_error'] = 'Пользователь не найден'
			return render_to_response('login.html', args)
	#else:
	#	if "pause" in request.session and request.POST:
	#		args['login_error'] = 'В последнее время вы слишком часто отправляли данные.'
	return render_to_response('login.html', args)


def logout(request):
	auth.logout(request)
	return redirect("/")


def main(request):
	if request.user.is_authenticated():
		return redirect("/profile/" + str(auth.get_user(request).username))
	return render_to_response('main.html', {'username' : auth.get_user(request).username})

def register(request):
	if request.user.is_authenticated():
		return redirect("/profile/" + str(auth.get_user(request).username))
	args = {}
	args.update(csrf(request))
	args['form'] = MyRegistrationForm()
	args['user_form'] = UserForm()
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		form = MyRegistrationForm(request.POST, request.FILES)
		if form.is_valid() and user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = form.save(commit=False)
			profile.user = user
			form.save()
			args['form'] = form
			args['user_form'] = user_form
			temp_user = User.objects.get(username=user_form.cleaned_data['username'])
			temp_user.is_active = False
			temp_user.save()
			#newuser = auth.authenticate(username=user_form.cleaned_data['username'], password=user_form.cleaned_data['password'])
			#auth.login(request, newuser)
			temp_user_profile = Users.objects.get(user_id=temp_user.id)
			temp_user_profile.user_key = gen_key()
			temp_user_profile.save()
			send_mail('Register at Shaire.ru', 'Click on the link for complete the registration on our site:) http://127.0.0.1:8000/auth/confirm_email/' + str(temp_user_profile.user_key) + '/', 'registration@shaire.ru', [str(temp_user.email)], fail_silently=False)
			return render_to_response('succes_register.html')
		else:
			form_errors = []
			for i in form.errors:
				form_errors.append([form.errors[i][0], i])
			user_form_errors = []
			if 'username' in user_form.errors: 
				user_form.errors['username'] = ['Такой логин уже существует']
			if 'password' in user_form.errors:
				user_form.errors['password'] = ['Пароль не удовлетворяет требованиям безопасности']
			if 'email' in user_form.errors:
				user_form.errors['email'] = ['Такой e-mail уже зарегистрирован']
			for i in user_form.errors:
				user_form_errors.append([user_form.errors[i][0], i])
			args['form_error'] = form_errors
			args['user_form_error'] = user_form_errors
	return render_to_response('register.html', args)

def confirm_email(request, user_key):
	user_profile = Users.objects.get(user_key=user_key)
	user = user_profile.user
	if not user.is_active:
		user.backend = 'django.contrib.auth.backends.ModelBackend'
		user.is_active = True
		user.save()
		auth.login(request, user)
		return redirect('/profile/' + str(user.username))
	else:
		return redirect('/')

def gen_key():
	alpha = 'qwertyuiopasdfghjklzxcvbnm'
	result = ''
	for i in range(30):
		result += alpha[random.randrange(0, 25, 1)]
	return result