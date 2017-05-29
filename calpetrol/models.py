from django.db import models

class Distance(models.Model):
    source_text = models.CharField(max_length=200)
    destination_text = models.CharField(max_length=200)
    distance = models.IntegerField(default=0)

    def __str__(self):
        return self.source_text
    def __str__(self):
        return self.destination_text
    def __int__(self):
        return self.distance

class Car(models.Model):
    car_type = models.CharField(max_length=200)
    car_use = models.IntegerField(default=0)
    def __str__(self):
        return self.car_type


# Create your models here.


