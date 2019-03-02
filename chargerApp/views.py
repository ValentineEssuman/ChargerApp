from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response


import time
# Create your views here.
def home(request):
    return render(request, 'chargerApp/index.html')

def chargePoint(request):
    #return HttpResponse("<h1>Charging App is Up and Running</h1>")
    #return render(request, 'dashboard/index.html')
    return render(request, 'dashboard/index.html')

#def viewCharts(request):
#    return render(request, 'dashboard/charts.html')

#Creating Charts
def get_data(request, *args, **kwargs):
    t=int(time.asctime().split()[3].split(":")[2])# genius nerdy code
    data = {
        "solar_value": str(t),
        "grid_value": str(t+1),
        "batt_value": str(t+2),
    }
    return JsonResponse(data) # http response



class ChartsData(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        t=int(time.asctime().split()[3].split(":")[2])
        labels =["Red", "Blue", "Yellow", "Green", "Purple", "Orange"]
        defaultItems = [2112, 231, 1121, 233, 125,2311,]
        data = {
                "labels": labels,
                "default": defaultItems,
                #"solar_value": str(t),
                #"grid_value": str(t+1),
                #"batt_value": str(t+2),
        }
        return Response(data)




#Reading and Displaying solar_power
def read_solarvalue(request):
    solar_power = request.POST["solar_power"]
    new_power = Power_source(value = solar_power)
    new_power.save()
    return "ok"

def display_solarvalue(request):
    solar_power = Power_source.objects.all()[0];
    return render(request,"index.html", {"solar_power":solar_power})
#
# #Reading and Displaying Grid power
# def read_gridvalue(request):
#     power = request.POST["power"]
#     new_power = Power_source(value = power)
#     new_power.save()
#     return "ok"
#
# def display_gridvalue(request):
#     grid_power = Power_source.objects.all()[0];
#     return render(request,"index.html", {"grid_power":grid_power})
#
# #Reading and Displaying Battery Gen power
# def read_battvalue(request):
#     batt_power = request.POST["batt_power"]
#     new_power = Power_source(value = batt_power)
#     new_power.save()
#     return "ok"
#
# def display_battvalue(request):
#     grid_power = Power_source.objects.all()[0];
#     return render(request,"index.html", {"grid_power":grid_power})
#
