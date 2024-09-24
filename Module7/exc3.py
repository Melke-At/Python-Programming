import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='password',
    autocommit=True
)

def insert_new_airport(airport_name, airport_icao):
    sql = "INSERT INTO airport (name, ident) VALUES (%s, %s)"
    cursor = connection.cursor()
    cursor.execute(sql, (airport_name, airport_icao))
    print(f"A new airport {airport_name} with ICAO code {airport_icao} has been added.")
    return

def get_airport_name(icao_code):
    sql = f"select name from airport where ident = '{icao_code}'"
    cursor = connection.cursor()
    cursor.execute(sql, (icao_code))
    airport_name = cursor.fetchone()
    if airport_name:
        return airport_name[0]
    else:
        return None

def register_airport_name():
    new_airport = input("Enter the name of new airport: ")
    icao_code = input("Enter ICAO code: ")

    if get_airport_name(icao_code):
        print(f"The ICAO code {icao_code} already exists in the database.")
    else:
        insert_new_airport(new_airport, icao_code)

def airport_information():
    icao_code = input("Enter ICAO code: ")
    airport_name = get_airport_name(icao_code)
    if airport_name:
        print(f"The name of the airport with ICAO code {icao_code} is: {airport_name}")
    else:
        print(f"There is no information available for ICAO code {icao_code}")

while True:
    print("\nAirport Data Program")
    print("A. Add a new airport")
    print("B. Fetch airport information")
    print("C. Quit")

    choice = input("Enter your choice (A/B/C): ").upper()
    if choice == "A":
        register_airport_name()
    elif choice == "B":
        airport_information()
    elif choice == "C":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice, please select A, B, or C.")
