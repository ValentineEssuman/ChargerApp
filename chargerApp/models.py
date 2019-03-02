from django.db import models
from django.http import HttpResponse
from django.utils import timezone

# Create your models here.

class Power_source(models.Model):
    # SOLAR
    source = models.CharField(max_length=64)
    switch = models.BooleanField(default = False)
    # SOLAR IS ON
    status = models.CharField(max_length=12)
    time_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.switch} - {self.source} - {self.status}-{self.time_on}"



class Connectivity(models.Model):
    power = models.ForeignKey(Power_source, on_delete=models.CASCADE,null=True,blank=True)
    #next_power = models.ForeignKey(Power_source, on_delete=models.CASCADE, related_name="altSources" )
    state = models.BooleanField(default = False)
    duration = models.IntegerField(default = 1)

    def __str__(self):
        return f"{self.power} -{self.state}"
    class Meta:
        verbose_name_plural="Connectivities"

#class User(models.Model):
