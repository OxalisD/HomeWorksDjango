from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)

class Measurements(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.PROTECT, related_name='sensor')
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(nullable=True)
