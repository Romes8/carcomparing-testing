from django.db import models

# Create your models here.
class Car(models.Model):
    id = models.IntegerField(primary_key=True)
    car_brand = models.CharField(max_length=20)
    car_model = models.CharField(max_length=20)
    car_description = models.CharField(max_length=70)
    engine_type = models.CharField(max_length=20)
    power = models.IntegerChoices
    tourque = models.IntegerChoices
    no_of_cylinder = models.IntegerField
    valves_per_cylinder = models.IntegerField
    transmission_type = models.CharField(max_length=20)
    drive_type = models.CharField(max_length=20)
    fuel_type = models.CharField(max_length=20)
    body_type = models.CharField(max_length=20)
    seating_capacity = models.IntegerField
    wheel_size = models.IntegerField
    top_speed = models.IntegerField
    acceleration_to_100 = models.DecimalField
    price = models.IntegerField()

class Images(models.Model):
    id = models.IntegerField
    link = models.CharField(max_length=70)
    car_id = models.ForeignKey('Car', on_delete=models.CASCADE)
