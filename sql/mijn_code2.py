import sqlite3
import get_all_cars

def get_destination_by_name(destination_name: str) -> int:
    # Maak verbinding met de database en haal de afstand op voor de opgegeven bestemmingsnaam
    conn = sqlite3.connect('travel.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT distance
        FROM destinations
        WHERE name = ?
    ''', (destination_name,))
    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0]
    else:
        raise ValueError(f"Bestemming '{destination_name}' niet gevonden in de database.")

def list_sahara_cars(destination_name: str) -> list:
    # Haal de afstand naar de bestemming op
    distance = get_destination_by_name(destination_name)

    # Haal alle auto's op
    cars = get_all_cars()

    # Filter de auto's die de afstand in één keer kunnen afleggen
    filtered_cars = [car for car in cars if car['usage'] * car['tankvolume'] >= distance]

    return filtered_cars

def print_suitable_cars(cars: list) -> None:
    # Print de lijst met geschikte auto's
    if not cars:
        print("Er zijn geen auto's die de afstand in één keer kunnen afleggen.")
    else:
        print("Geschikte auto's die de afstand in één keer kunnen afleggen:")
        for car in cars:
            print(f"Auto: {car['name']}, Verbruik: {car['usage']} L/km, Tankinhoud: {car['tankvolume']} L")

# Voorbeeldgebruik
try:
    cars = list_sahara_cars('Cairo')
    print_suitable_cars(cars)
except ValueError as e:
    print(e)