import mysql.connector

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = 'password',
    autocommit = True

)
def get_airport_by_ident(ICAO):
    sql = f"select*from airport where ident = '{ICAO}'"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result
code = input('type ICAO code: ')
airport = get_airport_by_ident(code)
if airport is not None:
    print(f'{airport[0]} is located in {airport[0]} in {airport[0]}')
else:
    print('airport not found')




