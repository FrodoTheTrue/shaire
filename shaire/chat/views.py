# -*- coding: utf-8 -*-
from django.shortcuts import render
from chat.models import UserInList
from chat.models import UserMessages
from django.contrib import auth
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.models import User
from loginsys.models import Accepted_Alerts
from django.http import HttpResponse
# Create your views here.


def chat_list(request):
	if not request.user.is_authenticated():
		return redirect('/')
	args = {}
	user = auth.get_user(request)

	# Info for header
	args['username'] = user.username
	all_invites = list(Accepted_Alerts.objects.filter(users=user))
	args['invites_count'] = len(all_invites)
	# End info for header

	args['users_list'] = []
	user = auth.get_user(request)
	all_message_users = list(UserInList.objects.filter(user_current = user))
	for i in all_message_users:
		args['users_list'].append(User.objects.get(id = i.user_message_to))
	return render_to_response('index.html', args)



def show_dialog(request, user_to):
	msg = []
	args = {}
	args['user_to_username'] = user_to
	current_user = auth.get_user(request)

	# Info for header
	args['username'] = current_user.username
	all_invites = list(Accepted_Alerts.objects.filter(users=current_user))
	args['invites_count'] = len(all_invites)
	# End info for header


	usr_to = User.objects.get(username = user_to)
	list_message = UserInList.objects.get(user_current = current_user, user_message_to = usr_to.id)
	messages_current = list(UserMessages.objects.filter(user_in_list = list_message))
	for i in messages_current:
		cr_usr = User.objects.get(id = i.now_user)
		avat = cr_usr.users.user_photo
		name = cr_usr.users.user_firstname
		famil = cr_usr.users.user_surname
		nick = cr_usr.username
		msg.append([i.text, avat, name, famil, nick])
	args['text_messages'] = msg
	args['users_list'] = []
	list_users = list(UserInList.objects.filter(user_current = current_user))
	for i in list_users:
		args['users_list'].append(User.objects.get(id = i.user_message_to))
	args['user_to'] = usr_to
	return render_to_response('messages.html', args)


def send_message(request):
	msg = ""
	current_user = auth.get_user(request)
	user_message = request.GET['text_message']
	user_name = request.GET['user_name']
	user_to = User.objects.get(username = user_name)
	list_with_user_one = UserInList.objects.get(user_current = current_user, user_message_to = user_to.id)
	list_with_user_two = UserInList.objects.get(user_current = user_to, user_message_to = current_user.id)
	new_message = UserMessages(text = user_message, now_user = current_user.id, user_in_list = list_with_user_one)
	new_message.save()
	new_message1 = UserMessages(text = user_message, now_user = current_user.id, user_in_list = list_with_user_two)
	new_message1.save()
	print(current_user.users.user_photo)
	msg += """
	<li class="media">
            <div class="media-body">
                <div class="media" id="msg_here">
                    <a class="pull-left" href="#">
                        <img class="media-object img-circle " style="height:65px; width:65px;" src=" """
	msg += '/static/' + str(current_user.users.user_photo)
	msg += """
     " />
                    </a>
                    <div class="media-body" > """
	msg += new_message.text
	msg += """
                    <br />
                    <small class="text-muted">"""
	msg += current_user.users.user_firstname + " " + current_user.users.user_surname
	msg += """
					</small>
                        <hr />
                    </div>
                </div>
            </div>
            </li>
	"""
	print(msg)
	return HttpResponse(msg)


def check_new(request):
	current_user = auth.get_user(request)
	count_was = request.GET['count']
	user_name = request.GET['user_to']
	usr_to = User.objects.get(username = user_name)
	list_with_user = UserInList.objects.get(user_current = current_user, user_message_to = usr_to.id)
	messages_now = UserMessages.objects.filter(user_in_list = list_with_user)
	count_now = 0
	for i in messages_now:
		count_now += 1
	if count_now - int(count_was) > 0:
		msg = ""
		cnt = count_now - int(count_was) - 1
		print(cnt)
		for i in range(len(messages_now) - 1 - cnt, len(messages_now)):
			id_user = messages_now[i].now_user
			user_msg = User.objects.get(id = id_user)
			msg += """
			<li class="media">
		            <div class="media-body">
		                <div class="media" id="msg_here">
		                    <a class="pull-left" href="#">
		                        <img class="media-object img-circle " style="height:65px; width:65px;" src=" """
			msg += '/static/' + str(user_msg.users.user_photo)
			msg += """
		     " />
		                    </a>
		                    <div class="media-body" > """
			msg += messages_now[i].text
			msg += """
		                    <br />
		                    <small class="text-muted">"""
			msg += str(user_msg.users.user_firstname) + " " + str(user_msg.users.user_surname)
			msg += """
							</small>
		                        <hr />
		                    </div>
		                </div>
		            </div>
		            </li>
			"""
		return HttpResponse(msg)
	else:
		return HttpResponse("-1")
