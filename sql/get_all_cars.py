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

all_cars = get_all_cars()
if all_cars:
    for car in all_cars:
        print(f"ID: {car[0]}, Brand: {car[1]}, Model: {car[2]}, Usage: {car[3]} km/l, Tank Volume: {car[4]} liters")
else:
    print("No cars found or an error occurred.")