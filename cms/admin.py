from django.contrib import admin

from .models import Incident, Assistance
# Register your models here.
admin.site.register(Incident)
admin.site.register(Assistance)