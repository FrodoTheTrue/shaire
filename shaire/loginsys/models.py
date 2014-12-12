# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser, User

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=UserManager.normalize_email(email),
            username=username)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email,
                                password=password,
                                username=username)
        user.is_admin = True
        user.save(using=self._db)
        return user

#class Users(AbstractBaseUser):
class Users(models.Model):
	class Meta:
		db_table = 'profile'
	user = models.OneToOneField(User)
	User._meta.get_field('email')._unique = True
	user_photo = models.ImageField(upload_to="static/avatars/", null=True, blank=True, default="/static/avatars/default_avatar.jpg")# default="images/default_avatar.jpg"
	user_firstname = models.CharField(max_length = 200)
	user_surname = models.CharField(max_length = 200)
	user_city = models.TextField()
	user_vk = models.TextField()
	user_key = models.CharField(max_length = 50)
	user_sex = models.CharField(max_length=2)
	user_birthday = models.DateField()
	is_active = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)



class Alerts(models.Model):
    class Meta:
        db_table = 'alerts'

    anonymous_alert = models.BooleanField(default=True)
    message = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    alert_to_user = models.ForeignKey(User)
    from_user_id = models.PositiveIntegerField()
    used = models.BooleanField(default=False)

class Accepted_Alerts(models.Model):
    class Meta:
        db_table = 'accepted_alerts'

    anonymous_alert = models.BooleanField(default=True)
    message = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(User)


