from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Medium(models.Model):
	name = models.CharField(max_length=200)
	medium_type = models.CharField(max_length = 200)

	def __unicode__(self):
		return self.name

class Reminder(models.Model):
	timespan = models.CharField(max_length=200)
	active = models.BooleanField()

	def __unicode__(self):
		return self.timespan

class Service(models.Model):
	name = models.CharField(max_length=200)
	medium = models.ManyToManyField(Medium, blank=True, null=True)

	def __unicode__(self):
		return self.name

class Contact(models.Model):
	name = models.CharField(max_length=200)
	reminder = models.ForeignKey(Reminder)

	def __unicode__(self):
		return self.name

class ContactAccount(models.Model):
	service = models.ForeignKey(Service)
	contact = models.ForeignKey(Contact)
	name = models.CharField(max_length=200)
	user_name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name

class UserAccount(models.Model):
	service = models.ForeignKey(Service)
	description = models.TextField()
	name = models.CharField(max_length=200)
	user = models.ForeignKey(User)
	user_name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name

class Interaction(models.Model):
	thread = models.CharField(max_length=200)
	reminder = models.ForeignKey(Reminder)
	contact_accounts = models.ManyToManyField(ContactAccount,blank=True, null=True)
	duration = models.IntegerField()
	interaction_type = models.CharField(max_length=50)

	def __unicode__(self):
		return self.thread

class Relationship(models.Model):
	interactions = models.ManyToManyField(Interaction, blank=True, null=True)
	relationship_type = models.CharField(max_length=50)
	user_profile = models.ForeignKey(User)

	def __unicode__(self):
		return self.relationship_type