def record ():
        names = set()
        while True:
            name = input("Enter new name or exit by pressing "" : ")
            if name == "":
                break
            if name in names:
                print("The name exists in the list: ")
            else:
                print("Enter New name")
                names.add(name)

        print("the name {name} in names are {Names}")
        for name in names:
             print(name)
record()


