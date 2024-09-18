import sqlite3

# Establish connection
connection = sqlite3.connect('event.db')
cursor = connection.cursor()

# Create tables
class Event:
    # ... (rest of the Event class remains the same)

    @classmethod
    def create_table(cls):
        sql_query = '''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT NOT NULL,
            date TEXT NOT NULL,
            start_time TEXT NOT NULL,
            end_time TEXT NOT NULL
        );
        '''
        cursor.execute(sql_query)
        connection.commit()

class Artist:
    # ... (rest of the Artist class remains the same)

    @classmethod
    def create_table(cls):
        sql_query = '''
        CREATE TABLE IF NOT EXISTS artists (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            gender TEXT NOT NULL,
            age INTEGER NOT NULL
        );
        '''
        cursor.execute(sql_query)
        connection.commit()

class Artistprofile:
    # ... (rest of the Artistprofile class remains the same)

    @classmethod
    def create_table(cls):
        sql_query = '''
        CREATE TABLE IF NOT EXISTS artist_profiles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            artist_id INTEGER NOT NULL,
            nationality TEXT NOT NULL,
            genre TEXT NOT NULL,
            influential_works TEXT NOT NULL,
            FOREIGN KEY(artist_id) REFERENCES artists(id)
        );
        '''
        cursor.execute(sql_query)
        connection.commit()

class Albums:
    # ... (rest of the Albums class remains the same)

    @classmethod
    def create_table(cls):
        sql_query = '''
        CREATE TABLE IF NOT EXISTS albums (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            artist_id INTEGER NOT NULL,
            album_name TEXT NOT NULL,
            release_year INTEGER NOT NULL,
            genre TEXT NOT NULL,
            number_of_tracks INTEGER NOT NULL,
            FOREIGN KEY(artist_id) REFERENCES artists(id)
        );
        '''
        cursor.execute(sql_query)
        connection.commit()

class attendance_capacity:
    # ... (rest of the attendance_capacity class remains the same)

    @classmethod
    def create_table(cls):
        sql_query = '''
        CREATE TABLE IF NOT EXISTS attendance_capacity (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            artist_id INTEGER NOT NULL,
            venue_name TEXT NOT NULL,
            attendance_capacity INTEGER NOT NULL,
            FOREIGN KEY(artist_id) REFERENCES artists(id)
        );
        '''
        cursor.execute(sql_query)
        connection.commit()

# Create tables
Event.create_table()
Artist.create_table()
Artistprofile.create_table()
Albums.create_table()
attendance_capacity.create_table()

# CLI
def main():
    while True:
        print("\n1. Add Event")
        print("2. Add Artist")
        print("3. Add Artist Profile")
        print("4. Add Album")
        print("5. Add Attendance Capacity")
        print("6. List Events")
        print("7. List Artists")
        print("8. List Artist Profiles")
        print("9. List Albums")
        print("10. List Attendance Capacity")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter event name: ")
            location = input("Enter event location: ")
            date = input("Enter event date: ")
            start_time = input("Enter event start time: ")
            end_time = input("Enter event end time: ")

            sql_query = "INSERT INTO events (name, location, date, start_time, end_time) VALUES (?, ?, ?, ?, ?)"
            cursor.execute(sql_query, (name, location, date, start_time, end_time))
            connection.commit()
            print("Event added successfully!")
            break

        elif choice == "2":
            name = input("Enter artist name: ")
            gender = input("Enter artist gender: ")
            age = input("Enter artist age: ")

            sql_query = "INSERT INTO artists (name, gender, age) VALUES (?, ?, ?)"
            cursor.execute(sql_query, (name, gender, age))
            connection.commit()
            print("Artist added successfully!")
            break

        elif choice == "3":
            artist_id = input("Enter artist ID: ")
            nationality = input("Enter artist nationality: ")
            genre = input("Enter artist genre: ")
            influential_works = input("Enter artist influential works: ")

            sql_query = "INSERT INTO artist_profiles (artist_id, nationality, genre, influential_works) VALUES (?, ?, ?, ?)"
            cursor.execute(sql_query, (artist_id, nationality, genre, influential_works))
            connection.commit()
            print("Artist profile added successfully!")
            break

        elif choice == "4":
            artist_id = input("Enter artist ID: ")
            album_name = input("Enter album name: ")
            release_year = input("Enter album release year: ")
            genre = input("Enter album genre: ")
            number_of_tracks = input("Enter album number of tracks: ")

            sql_query = "INSERT INTO albums (artist_id, album_name, release_year, genre, number_of_tracks) VALUES (?, ?, ?, ?, ?)"
            cursor.execute(sql_query, (artist_id, album_name, release_year, genre, number_of_tracks))
            connection.commit()
            print("Album added successfully!")
            break

        elif choice == "5":
            artist_id = input("Enter artist ID: ")
            venue_name = input("Enter venue name: ")
            attendance_capacity = input("Enter attendance capacity: ")

            sql_query = "INSERT INTO attendance_capacity (artist_id, venue_name, attendance_capacity) VALUES (?, ?, ?)"
            cursor.execute(sql_query, (artist_id, venue_name, attendance_capacity))
            connection.commit()
            print("Attendance capacity added successfully!")
            break

        elif choice == "6":
            sql_query = "SELECT * FROM events"
            cursor.execute(sql_query)
            result = cursor.fetchall()
            for row in result:
                print(row)

        elif choice == "7":
            sql_query = "SELECT * FROM artists"
            cursor.execute(sql_query)
            result = cursor.fetchall()
            for row in result:
                print(row)

        elif choice == "8":
            sql_query = "SELECT * FROM artist_profiles"
            cursor.execute(sql_query)
            result = cursor.fetchall()
            for row in result:
                print(row)

        elif choice == "9":
            sql_query = "SELECT * FROM albums"
            cursor.execute(sql_query)
            result = cursor.fetchall()
            for row in result:
                print(row)

        elif choice == "10":
            sql_query = "SELECT * FROM attendance_capacity"
            cursor.execute(sql_query)
            result = cursor.fetchall()
            for row in result:
                print(row)

        elif choice == "11":
            print("Completed. Thank you for using the event management system!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()