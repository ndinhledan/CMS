from django import forms
from .models import Incident, Comment
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin



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
			'caller',
			)

class MessageForm(PopRequestMixin, CreateUpdateAjaxMixin,forms.ModelForm):
        class Meta:
                model = Incident
                fields = ('message',)

