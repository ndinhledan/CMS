'''
TODO
filter
view all cases (closed and open)
form caller, submitter
closed by
'''



from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import logout

from .models import Incident
from .forms import IncidentForm
from .location import getCoordinates
from .filters import IncidentFilter
# Create your views here.

class IndexView(LoginRequiredMixin, generic.ListView):
	model = Incident

	context_object_name = 'incident_list'
	template_name = 'cms/index.html'

	conditions ={
		"severity": "severity",
		"date" : "incident_date__date"
	}

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['filter'] = IncidentFilter(self.request.GET,queryset=self.get_queryset())
		return context


class CreateIncidentView(LoginRequiredMixin, generic.TemplateView):
	template_name = 'cms/createincident.html'

	def get(self, request):
		form = IncidentForm()
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = IncidentForm(request.POST)
		if form.is_valid():
			incident = form.save(commit=False)

			location = form.cleaned_data['street_name'] + " " + form.cleaned_data['apartment_number'] +" " + form.cleaned_data['postal_code']

			incident.location = location
			incident.submitter = request.user
			incident.lat, incident.long = getCoordinates(int(form.cleaned_data['postal_code']))
			incident.save()
			return HttpResponseRedirect(reverse('cms:home'))
		return render(request, self.template_name, {'form': form})

class DetailCase(generic.DetailView):
	template_name = 'cms/detail_case.html'
	model = Incident


	def post(self, request, pk):
		self.object = self.get_object()
		self.object.is_closed = True
		self.object.incident_closed_date = timezone.now()
		self.object.save()
		messages.info(request, "Case " + str(self.object.id) + " has been closed successfully")
		return redirect('cms:home')

		return render(request, "cms/closed_confirm.html")

from API.weather import *

def mapview(request):

	psi_north = getPSI('north')
	psi_south = getPSI('south')
	psi_east = getPSI('east')
	psi_west = getPSI('west')
	psi_central = getPSI('central')
	weather = getWeather()

	context = {
        'psi_north': psi_north,
        'psi_south': psi_south,
        'psi_east': psi_east,
        'psi_west': psi_west,
		'psi_central': psi_central,
		'weather_north': weather['North'],
        'weather_south': weather['South'],
        'weather_east': weather['East'],
        'weather_west': weather['West'],
		'weather_central': weather['Central'],
    }

    # Render the HTML template cms/view-map.html with the data in the context variable
	return render(request, 'cms/view-map.html', context=context)