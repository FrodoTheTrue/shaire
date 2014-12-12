# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.core.context_processors import csrf
from loginsys.models import Users, Accepted_Alerts
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.

def search(request):
	args = {}
	args.update(csrf(request))
	user = auth.get_user(request)

	# Info for header
	args['username'] = user.username
	all_invites = list(Accepted_Alerts.objects.filter(users=user))
	args['invites_count'] = len(all_invites)
	# End info for header

	if request.POST:
		search_username = request.POST['search_username']
		search_firstname = request.POST['search_firstname']
		search_surname = request.POST['search_surname']
		try:
			search_gender = request.POST['search_gender']
		except MultiValueDictKeyError:
			search_gender = ''
		print(search_username, search_firstname, search_surname, search_gender)
		return show_result(request, search_username, search_firstname, search_surname, search_gender)

	return render_to_response('search.html', args)

def show_result(request, search_username, search_firstname, search_surname, search_gender):
	args = {}
	find_smn = False
	args['found_users'] = []
	user = auth.get_user(request)
	if search_gender == 'male':
		search_gender = "М"
	if search_gender == 'female':
		search_gender = "Ж"

	# Info for header
	args['username'] = user.username
	all_invites = list(Accepted_Alerts.objects.filter(users=user))
	args['invites_count'] = len(all_invites)
	# End info for header

	if search_username != '':
		try:
			args['found_users'].append(User.objects.get(username=search_username))
			find_smn = True
		except User.DoesNotExist:
			pass
	else:
		if search_firstname == '' and search_surname == '' and search_gender == '':
			res_set = set(Users.objects.all())
		elif search_firstname != '' and search_surname != '':
			res_set = set(Users.objects.filter(user_firstname=search_firstname, user_surname=search_surname))
		elif search_firstname != '' and search_gender != '':
			res_set = set(Users.objects.filter(user_firstname=search_firstname, user_sex=search_gender))
		elif search_surname != '' and search_gender != '':
			res_set = set(Users.objects.filter(user_surname=search_surname, user_sex=search_gender))
		elif search_surname != '':
			res_set = set(Users.objects.filter(user_surname=search_surname))
		elif search_gender != '':
			res_set = set(Users.objects.filter(user_sex=search_gender))
		elif search_firstname != '':
			res_set = set(Users.objects.filter(user_firstname=search_firstname))
		for i in res_set:
			args['found_users'].append(i.user)

	if len(args['found_users']) != 0:
		find_smn = True
	args['find_smn'] = find_smn
	return render_to_response('results.html', args)