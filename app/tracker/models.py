from django.db import models
from django.contrib.auth.models import User

MEDIUM_CHOICES = (
    (1, u'Email'),
    (2, u'Text'),
    (3, u'IM'),
    (4, u'Phone'),
    (5, u'Facebook'),
    (6, u'In Person'))

# Generic Models
class Service(models.Model):
	name = models.CharField(max_length=200)
	medium = models.IntegerField(choices=MEDIUM_CHOICES, blank=True, null=True)

	def __unicode__(self):
		return self.name

# Users contacts models

class Contact(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class ContactAccount(models.Model):
    contact = models.ForeignKey(Contact)
    service = models.ForeignKey(Service)
    description = models.TextField()
    name = models.CharField(max_length=200)
    account_id = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


# Items connecting users and their contacts

class Interaction(models.Model):
    source = models.ForeignKey(ContactAccount,related_name="%(app_label)s_%(class)s_source")
    destination = models.ManyToManyField(ContactAccount,related_name="%(app_label)s_%(class)s_destination")
    #duration = models.IntegerField()
    interaction_type = models.CharField(max_length=50)

    def __unicode__(self):
        return self.thread

class Relationship(models.Model):
	interactions = models.ManyToManyField(Interaction, blank=True, null=True)
	relationship_type = models.CharField(max_length=50)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.relationship_type

# Reminders

class Reminder(models.Model):
	active = models.BooleanField()

	def __unicode__(self):
		return self.timespan


