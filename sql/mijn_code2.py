import sqlite3
#import get_all_cars

def get_all_cars() -> list:
    # Voorbeeldimplementatie: zorg ervoor dat het een lijst van woordenboeken retourneert
    return [
        {'name': 'Auto A', 'usage': 0.08, 'tankvolume': 50},
        {'name': 'Auto B', 'usage': 0.1, 'tankvolume': 60},
        {'name': 'Auto C', 'usage': 0.06, 'tankvolume': 40},
        # Voeg meer auto's toe indien nodig
    ]

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
    cars = get_all_cars()  # Dit roept de functie get_all_cars() aan

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