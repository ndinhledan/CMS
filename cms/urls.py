from django.urls import path, include

from django.contrib.auth.views import LoginView
from . import views

app_name = 'cms'

urlpatterns =[
	path('', views.IndexView.as_view(), name='home'),
	path('accounts/', include('django.contrib.auth.urls'), name='login'),
	path('create-incident/', views.CreateIncidentView.as_view(),name='create-incident'),
	path('case/<int:pk>/', views.DetailCase.as_view(), name='case'),
	path('order/by_<condition>', views.IndexView.as_view(), name='order'),
	path('view-map/', views.MapView.as_view(), name='view-map'),
  	path('send-message/', views.MessageCreateView.as_view(), name = 'send_message'),
]

