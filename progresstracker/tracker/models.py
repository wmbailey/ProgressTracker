from django.db import models

# Create your models here.
class Goal(models.Model):
	statement = models.CharField(max_length=200)