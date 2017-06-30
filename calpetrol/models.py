from django.db import models
from django.contrib.auth.models import User
import datetime

class Distance(models.Model):
    source_text = models.CharField(max_length=200)
    destination_text = models.CharField(max_length=200)
    distance = models.IntegerField(default=0)

    def __str__(self):
        return "%s %s" % (self.source_text, self.destination_text)
        

class Car(models.Model):
    car_type = models.CharField(max_length=200)
    car_use = models.IntegerField(default=0)
    def __str__(self):
        return self.car_type

class User_data(models.Model):
    user = models.ForeignKey(User,null=True)
    source_destination = models.ForeignKey(Distance,null=True)
    car = models.ForeignKey(Car,null=True)
    petrol_cost = models.FloatField(default=0)
    cost = models.FloatField(default=0)
    date = models.DateField(("Date"), default=datetime.date.today)


    def __unicode__(self):
        return self.user
   

# Create your models here.


