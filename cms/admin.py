from django.contrib import admin

from django.contrib.auth.models import User

from .models import Incident, Assistance
# Register your models here.
admin.site.register(Incident)
admin.site.register(Assistance)