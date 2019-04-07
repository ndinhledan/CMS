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
			'mobile_number',
		)

	def clean_postal_code(self):
		postal_code = self.cleaned_data['postal_code']
		try:
			code = int(postal_code)
			if code // 100000 == 0 or code//100000 > 9:
				raise forms.ValidationError('Postal code is a 6 digits number')
		except ValueError:
			raise forms.ValidationError('Postal code is a 6 digits number')

class MessageForm(PopRequestMixin, CreateUpdateAjaxMixin,forms.ModelForm):
        class Meta:
                model = Incident
                fields = ('message',)

