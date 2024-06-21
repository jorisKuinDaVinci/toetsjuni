from get_all_cars import *
from get_destination_by_name import *
import sqlite3

def list_sahara_cars(destination_name: str) -> list:
    cars = []
    # code om de afstand op te zoeken in de tabel destinations
    conn = sqlite3.connect("travel.db")
    cursor = conn.cursor()
    cursor.execute('''
        SELECT distance
        FROM destinations
        WHERE name = ?
    ''', (destination_name,))
    distance = cursor.fetchone()[0]
    conn.close()
 
    # code om de cars te selecteren die de afstand in één keer kunnen overbruggen
    cars = get_all_cars()
    filtered_cars = [car for car in cars if car["usage"] * car["tankvolume"] >= distance]

    return filtered_cars
 
# code om de cars te selecteren die de afstand in één keer kunnen overbruggen
 
cars = list_sahara_cars("Cairo")