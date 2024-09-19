import mysql.connector
from geopy.distance import geodesic


connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = 'password',
    autocommit = True
)

def get_location_by_ICAO (ICAO):
    sql = f"select latitude_deg, longitude_deg from airport where ident = '{ICAO}'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        return(result[0], result[1])
    else:
        print(f"No airport found with ICAO code: {ICAO}")
        return None
def calculate_distance_between_airport(code1,code2):
    code1 = get_location_by_ICAO(code1)
    code2 = get_location_by_ICAO(code2)
    if code1 and code2:
        distance = geodesic(code1, code2).kilometers
        print(f"The distance between {code1} and {code2} is {distance} km")


    else:
        print("unable to print the distance due to the missing data")
code1 = input("Enter the first ICAO code: ")
code2 = input("Enter the second ICAO code: ")
calculate_distance_between_airport(code1, code2)
connection.close()
