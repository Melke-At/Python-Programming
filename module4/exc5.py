user_name = str (input("Enter user name : "))
password = str (input("Enter password : "))
count=0
if user_name != "phyton" and password != "rules":
    while count < 5:
        print ("enter the username and password again: ")
        user_name = str(input("Enter user name : "))
        password = str(input("Enter password : "))
        count = count + 1
    print("Access Denied!")
else:
    print("Welcome")








