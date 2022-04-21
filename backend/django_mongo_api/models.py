from django.db import models

# Create your models here.    
class Test(models.Model):
    title = models.CharField(max_length=200, blank=False, default='')
    content = models.CharField(max_length=200,blank=False, default='')
    
    class Meta:
        db_table = 'test'

class Sensor(models.Model):
    temperature = models.IntegerField(blank=False, default=25)
    moisture = models.IntegerField(blank=False, default=50)
    humidity = models.IntegerField(blank=False, default=50)
    air_vent = models.BooleanField(blank=False, default=True)
    water_pump = models.BooleanField(blank=False, default=False)
    
    class Meta:
        db_table = 'sensor'
    
    