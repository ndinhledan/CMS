'''
TODO
filter 
view all cases (closed and open)
form caller, submitter
closed by
'''






from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Incident
from .forms import IncidentForm
# Create your views here.

class IndexView(LoginRequiredMixin, generic.ListView):
	model = Incident

	context_object_name = 'incident_list'
	template_name = 'cms/index.html'

	def get_queryset(self):
		return Incident.objects.filter(is_closed=False).order_by('-incident_date')

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
		return render(request, "cms/closed_confirm.html")

class MapView(LoginRequiredMixin, generic.TemplateView):
	template_name = 'cms/view-map.html'