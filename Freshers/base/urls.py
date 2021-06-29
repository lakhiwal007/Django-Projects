from django.urls import path
from .views import *

app_name = 'Freshers'
urlpatterns = [
    path('aboutme/',aboutme_view),
    path('studymaterial/',studymaterial_view),
    path('studentcorner/',studentcorner_view),
    path('campusinfo/',campusinfo_view),
    path('InstituteCore/',institutecore_view),
    path('HSS/',HSS_view),
    path('ESOs/',ESOs_view),
]
