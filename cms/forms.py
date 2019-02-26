from django import forms
from .models import Incident
class IncidentForm(forms.ModelForm):
	street_name = forms.CharField()
	apartment_number = forms.CharField()
	postal_code = forms.CharField()

	class Meta:
		model = Incident
		fields = (
			'incident_type',
			'assistance_type',
			'severity',
			)