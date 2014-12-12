# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, render_to_response
from loginsys.models import Users, Alerts, Accepted_Alerts
from django.contrib.auth.models import User
from django.contrib import auth
from user_profile.views import find_age, ChangeAvatar
from django.core.context_processors import csrf
from chat.models import UserInList
# Create your views here.

def send_invite(request, user_id, type_message):
	user_to = User.objects.get(id = user_id)
	all_alerts = Alerts.objects.all()
	print(all_alerts)
	user_self = auth.get_user(request)
	for i in all_alerts:
		if i.alert_to_user == user_self and i.message == type_message and not i.used:
			alert = Alerts(alert_to_user=user_to, message=type_message, from_user_id=user_self.id, used=True)
			alert.save()
			accepted_alert = Accepted_Alerts.objects.create(message=type_message)
			accepted_alert.users.add(user_to, user_self)
			accepted_alert.save()

			#Add user to chat list
			new_chat = UserInList(user_current = user_self, user_message_to = user_to.id)
			new_chat.save()
			new_chat_to = UserInList(user_current = user_to, user_message_to = user_self.id)
			new_chat_to.save()
			#######


			i.used = True
			i.save()
			return redirect("/profile/" + str(user_to.username))
		if i.alert_to_user == user_to and i.message == type_message and not i.used:
			return redirect("/profile/" + str(user_to.username))
	alert = Alerts(alert_to_user=user_to, message=type_message, from_user_id=user_self.id)
	alert.save()
	return redirect("/profile/" + str(user_to.username))


def check_invites(request):
	args = {}
	args.update(csrf(request))
	args['form_change_avatar'] = ChangeAvatar()
	user = auth.get_user(request)
	args['my_page'] = True
	args['username'] = user.username
	args['user'] = user
	args['user_profile'] = user.users
	birthday = args['user_profile'].user_birthday
	age = find_age(birthday)
	args['user_age'] = age[0]
	args['user_age_word'] = age[1]
	all_invites = list(Accepted_Alerts.objects.filter(users=user))
	args['invites_count'] = len(all_invites)
	accepted_invites = []
	for invite in all_invites:
		users = invite.users.all()
		for i in users:
			if i != user:
				accepted_invites.append({'message' : invite.message,'user' : i, 'date' : invite.date, 'user_profile' : i.users})
	accepted_invites.reverse()
	args['accepted_invites'] = accepted_invites
	return render_to_response('my_invites.html', args)