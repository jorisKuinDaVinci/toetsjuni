import sqlite3

def get_all_cars():
    try:
        with sqlite3.connect('travel.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM cars')
            cars = cursor.fetchall()
            return cars
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []


def get_destination_by_name(destination_name: str) -> int:
    try:
        with sqlite3.connect('travel.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT distance
                FROM destinations
                WHERE name = ?
            ''', (destination_name,))
            result = cursor.fetchone()

            if result:
                return result[0]
            else:
                raise ValueError(f"Bestemming '{destination_name}' niet gevonden in de database.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return 0

def list_sahara_cars(destination_name: str) -> list:
    # Haal de afstand naar de bestemming op
    distance = get_destination_by_name(destination_name)

    try:
        distance = int(distance)  # Zorg ervoor dat distance een integer is
    except (TypeError, ValueError):
        raise ValueError(f"Afstand naar bestemming '{destination_name}' is niet geldig.")

    # Haal alle auto's op
    cars = get_all_cars()

    # Filter de auto's die de afstand in één keer kunnen afleggen
    filtered_cars = []
    for car in cars:
        try:
            usage = int(car[1])  # Zorg ervoor dat usage een integer is
            tankvolume = int(car[2])  # Zorg ervoor dat tankvolume een integer is
            if usage * tankvolume >= distance:
                filtered_cars.append(car)
        except (TypeError, ValueError):
            continue

    return filtered_cars

def print_suitable_cars(cars: list) -> None:
    # Print de lijst met geschikte auto's
    if not cars:
        print("Er zijn geen auto's die de afstand in één keer kunnen afleggen.")
    else:
        print("Geschikte auto's die de afstand in één keer kunnen afleggen:")
        for car in cars:
            print(f"Auto: {car['name']}, Verbruik: {car['usage']} L/km, Tankinhoud: {car['tankvolume']} L")

# voeg dordrecht toe als bestemming
def add_destination(name: str, distance: int) -> None:
    try:
        with sqlite3.connect('travel.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO destinations (name, distance)
                VALUES (?, ?)
            ''', (name, distance))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")

add_destination('Dordrecht', 1)
# Voorbeeldgebruik
try:
    cars = list_sahara_cars('Tripoli')
    print_suitable_cars(cars)
except ValueError as e:
    print(e)