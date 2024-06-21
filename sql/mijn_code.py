from get_all_cars import get_all_cars
from get_destination_by_name import get_destination

def list_sahara_cars(destination_name: str) -> list:
    cars = []
    # code om de afstand op te zoeken in de tabel destinations
    destination = get_destination(destination_name)
    distance = destination['distance']
    # code om de cars te selecteren die de afstand in één keer kunnen overbruggen
    for car in get_all_cars():
        if car['max_distance'] >= distance:
            cars.append(car)
 
    return cars
 
# code om de cars te selecteren die de afstand in één keer kunnen overbruggen
 
cars = list_sahara_cars('Cairo')