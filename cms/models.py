from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Assistance(models.Model):
	number = models.CharField(
		max_length=8)
	name = models.CharField(
		max_length=50)

	def __str__(self):
		return self.name
	
class Comment(models.Model):
        Message = models.CharField(max_length = 200)

        def __str__(self):
                return self.Message
class Incident(models.Model):
	Fire = 'FIR'
	Haze = 'HAZ'
	Bird = 'BIR'
	Tsunami = 'TSU'
	Aftershock = 'AFT'
	Terrorist = 'TER'

	INCIDENT_TYPE_CHOICES = (
		(Fire,'Fire outbreak'),
		(Haze, 'Haze'),
		(Bird, 'Bird flu outbreak'),
		(Tsunami, 'Tsunami'),
		(Aftershock, 'Earthquake Aftershock'),
		(Terrorist, 'Terrorist Activity')
	)

	submitter = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		null=True)

	caller = models.CharField(
		max_length=50,
		default='Anonymous')

	incident_type = models.CharField(
		max_length=3,
		choices=INCIDENT_TYPE_CHOICES,
		)

	incident_date = models.DateTimeField('date incident happens',
											auto_now_add=True)
	
	assistance_type = models.ForeignKey(
		Assistance,
		on_delete=models.CASCADE)

	severity = models.IntegerField(default=1,
		choices=(
			(1,'1'),
			(2,'2'),
			(3,'3'),
			(4,'4'),
			(5,'5'),
			))

	location = models.TextField(default ='Singapore')

	is_closed = models.BooleanField(default=False)

	incident_closed_date = models.DateTimeField(null=True)

	lat = models.FloatField(null=True)
	long = models.FloatField(null=True)

	class Meta:
		ordering = ["-incident_date"]


