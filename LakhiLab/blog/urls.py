from django.urls import path
from .views import *

urlpatterns = [
	path('',home_view,name='home'),
	path('<pk>/',blogDetail_view,name='blog'),
]