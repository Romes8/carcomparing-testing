from django.http.response import HttpResponse
from cars.models import Car, Image
import datetime

#get all data from a car model
def get_car(car):
    count = 0
    data = []
    carres = Car.objects.get(car_model=car)
    print(carres.id)
    car_id = Image.objects.filter(car_id_id=carres.id)
    
    print(carres.car_model)

    data.append({
        "brand": carres.car_brand,
        "model": carres.car_model,
        "description": carres.car_description,
        "engine": carres.engine_type,
        "power": carres.power,
        "torque": carres.tourque,
        "cylinders": carres.no_of_cylinder,
        "valves": carres.valves_per_cylinder,
        "transmission": carres.transmission_type,
        "drive_type": carres.drive_type,
        "fuel": carres.fuel_type,
        "body": carres.body_type,
        "seats": carres.seating_capacity,
        "wheels": carres.wheel_size,
        "top_speed": carres.top_speed,
        "acceleration": carres.acceleration_to_100,
        "price": carres.price,
    })
    
    for im in car_id:
        data.append({
            "image": im.link,
        })
        print("once")
        break
    
    print("Ended")
    return data


