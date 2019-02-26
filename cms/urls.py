from django.urls import path, include

from django.contrib.auth.views import LoginView
from . import views

app_name = 'cms'

urlpatterns =[
	path('', views.IndexView.as_view(), name='home'),
	path('accounts/', include('django.contrib.auth.urls'), name='login'),
	path('create-incident/', views.CreateIncidentView.as_view(),name='create-incident'),
]