from django.shortcuts import render
from django.urls import path
from .views import get_data,ChartsData

from . import views

urlpatterns = [
    path("", views.home),
    path("charging/", views.chargePoint),
    path("api/data/", get_data, name='api-data'),
    path("charts/data/", ChartsData.as_view()),

    #urls for links data
    #path("data/", views.read_solarvalue, name = "read_solar"),

    #urls to power sources
    #path("checkS_power/", views.read_solarvalue, name = "read_solar"),
    #path("displayS_power/",views.display_solarvalue,name = "display_solar"),

    # path("checkG_power/", views.read_gridvalue, name = "read_Grid"),
    # path("displayG_power/",views.display_gridvalue,name = "display_Grid"),
    #
    # path("checkB_power/", views.read_gridvalue, name = "read_Batt"),
    # path("displayB_power/",views.display_gridvalue,name = "display_Batt")

]
