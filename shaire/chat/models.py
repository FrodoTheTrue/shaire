from django.db import models
from loginsys.models import Users
from django.contrib.auth.models import User
# Create your models here.

class UserInList(models.Model):
	class Meta:
		db_table = "chat_list"
	user_current = models.ForeignKey(User)
	user_message_to = models.PositiveIntegerField()


class UserMessages(models.Model):
	class Meta:
		db_table = "user_messages"
	user_in_list = models.ForeignKey(UserInList)
	now_user = models.PositiveIntegerField()
	text = models.TextField()