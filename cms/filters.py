from .models import Incident
from django import forms
import django_filters

class IncidentFilter(django_filters.FilterSet):
    incident_day = django_filters.DateFilter(field_name='incident_date',
                                            lookup_expr='date',
                                            input_formats=['%m/%d/%Y'],
                                            widget=forms.DateInput({'class': 'datepicker'}),
                                            label='Date of Incident')
    class Meta:
        model = Incident
        fields = (
            'id',
			'assistance_type',
			'severity',
            'incident_day',
			)
