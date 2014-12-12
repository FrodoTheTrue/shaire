# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from loginsys.models import Users, Alerts, Accepted_Alerts
from django.contrib.auth.models import User
import datetime
from user_profile.forms import ChangeAvatar, ChangeName, ChangeSecondName, ChangeSex, ChangeCity, ChangeBirthday, ChangeVK
from django.core.context_processors import csrf
# Create your views here.

def profile(request, username):
	if not request.user.is_authenticated():
		return redirect('/')
	args = {}
	args.update(csrf(request))
	args['form_change_avatar'] = ChangeAvatar()
	args['my_page'] = False
	user = auth.get_user(request)
	args['username'] = user.username
	if args['username'] == username:
		args['my_page'] = True
	args['browsable_user'] = User.objects.get(username=username)
	args['user_profile'] = args['browsable_user'].users
	birthday = args['user_profile'].user_birthday
	all_invites = list(Accepted_Alerts.objects.filter(users=user))
	args['invites_count'] = len(all_invites)
	age = find_age(birthday)
	args['user_age'] = age[0]
	args['user_age_word'] = age[1]
	args['invites'] = Alerts.objects.filter(alert_to_user=args['browsable_user'].id)
	args['invites'] = list(args['invites'])
	args['invites'].reverse()
	return render_to_response('profile.html', args)

def settings(request):
	args = {}
	args.update(csrf(request))
	user = auth.get_user(request)
	all_invites = list(Accepted_Alerts.objects.filter(users=user))
	args['invites_count'] = len(all_invites)
	args['username'] = user.username
	args['user'] = user
	args['user_profile'] = args['user'].users
	args['change_name_form'] = ChangeName()
	args['change_second_name_form'] = ChangeSecondName()
	args['change_sex_form'] = ChangeSex()
	args['change_city_form'] = ChangeCity()
	args['change_birthday_form'] = ChangeBirthday()
	args['change_vk_form'] = ChangeVK()
	return render_to_response('settings.html', args)

def find_age(birthday):
	cur_date = str()
	now = str(datetime.datetime.now())
	for s in now:
		if not s == ' ':
			cur_date += (s)
		else:
			break
	birthday = str(birthday)
	temp = []
	for letter in range(len(cur_date)):
		if cur_date[letter] == '-':
			temp.append(letter)
	cur_year = int(cur_date[:temp[0]])
	cur_month = int(cur_date[temp[0] + 1:temp[1]])
	cur_day = int(cur_date[temp[1] + 1:temp[1] + 3])

	temp = []
	for letter in range(len(birthday)):
		if birthday[letter] == '-':
			temp.append(letter)
	birthday_year = int(birthday[:temp[0]])
	birthday_month = int(birthday[temp[0] + 1:temp[1]])
	birthday_day = int(birthday[temp[1] + 1:temp[1] + 3])

	age = cur_year - birthday_year
	if cur_month < birthday_month:
		age -= 1
	elif cur_month == birthday_month:
		if cur_day < birthday_day:
			age -= 1
	age_last_number = int(str(age)[len(str(age)) - 1])
	if age_last_number >= 5 or age_last_number == 0 or (age in {11, 12, 13, 14}):
		age_word = "лет"
	elif age_last_number == 1:
		age_word = "год"
	else:
		age_word = "года"
	return (age, age_word)


def change_avatar(request):
	if request.method == 'POST':
		form = ChangeAvatar(request.POST, request.FILES)
		user = auth.get_user(request)
		user_profile = user.users
		if "default_avatar.jpg" not in str(user_profile.user_photo):
			user_profile.user_photo.delete()
		user_profile.user_photo = request.FILES['user_photo']
		user_profile.save()
		return redirect('/')


def change_name(request):
	if request.method == 'POST':
		form = ChangeName(request.POST)
		if form.is_valid():
			username = auth.get_user(request).username
			user = User.objects.get(username=username)
			user_profile = user.users
			user_profile.user_firstname = request.POST['user_firstname']
			user_profile.save()
			return redirect('/profile/settings/')
		else:
			return redirect('/profile/settings/')



def change_secondname(request):
	if request.method == 'POST':
		form = ChangeSecondName(request.POST)
		if form.is_valid():
			username = auth.get_user(request).username
			user = User.objects.get(username=username)
			user_profile = user.users
			user_profile.user_surname = request.POST['user_surname']
			user_profile.save()
			return redirect('/profile/settings/')
		else:
			return redirect('/profile/settings/')


def change_sex(request):
	if request.method == 'POST':
		form = ChangeSex(request.POST)
		if form.is_valid():
			username = auth.get_user(request).username
			user = User.objects.get(username=username)
			user_profile = user.users
			user_profile.user_sex = request.POST['user_sex']
			user_profile.save()
			return redirect('/profile/settings/')
		else:
			return redirect('/profile/settings/')


def change_city(request):
	if request.method == 'POST':
		form = ChangeCity(request.POST)
		if form.is_valid():
			username = auth.get_user(request).username
			user = User.objects.get(username=username)
			user_profile = user.users
			user_profile.user_city = request.POST['user_city']
			user_profile.save()
			return redirect('/profile/settings/')
		else:
			return redirect('/profile/settings/')



def change_vk(request):
	if request.method == 'POST':
		form = ChangeVK(request.POST)
		if form.is_valid():
			username = auth.get_user(request).username
			user = User.objects.get(username=username)
			user_profile = user.users
			user_profile.user_vk = request.POST['user_vk']
			user_profile.save()
			return redirect('/profile/settings/')
		else:
			return redirect('/profile/settings/')

def change_birthday(request):
	return redirect('/profile/settings/')

