import mysql.connector

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = 'password',
    autocommit = True

)
def get_airport_name(icao):
    sql = f"select name from airport where ident='{icao}'"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    return result


def display_menu(choice):
    print ("Enter your choice")
    choice = [1, 2, 3]

    for i in range(len(choice)):
       print ({choice[i]})

def get_user_choice():
    while True:
        display_menu(1)
        choice = input("Enter the number of your choice: ")
        if choice == 1:
            newcode = input(f'Enter new airport icao code: ')
            newname = input(f'Enter new airport name: ')
            print (f"you have entered new airport with the code {newcode} and name{newname} ")
        elif choice == 2:
            airport_code = input(f"Do you want to fetch from the existing airport ")
            get_airport_name(airport_code)
        elif choice == 3:
            break

get_user_choice()




