from django.db import models

# Create your models here.
class Assistance(models.Model):
	number = models.CharField(
		max_length=8)
	name = models.CharField(
		max_length=50)

	def __str__(self):
		return self.name

class Incident(models.Model):
	Fire = 'FIR'
	Haze = 'HAZ'
	Cat_on_tree = 'CAT'
	Tsunami = 'TSU'

	INCIDENT_TYPE_CHOICES = (
		(Fire,'Fire'),
		(Haze, 'Haze'),
		(Cat_on_tree, 'Cat on a tree'),
		(Tsunami, 'Tsunami'),
	)

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

	class Meta:
		ordering = ["-incident_date"]


