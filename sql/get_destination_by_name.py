import sqlite3

def get_destination(destination_name):
    try:
        with sqlite3.connect('travel.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM destinations WHERE name = ?', (destination_name,))
            destination = cursor.fetchone()
            return destination
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None

destination_name = 'Cairo'
destination = get_destination(destination_name)
if destination:
    print(f"ID: {destination[0]}, Name: {destination[1]}, Distance: {destination[2]} km")
else:
    print(f"Destination '{destination_name}' not found.")