class Publication:

    def __init__(self, name):
        self.name = name

    def print_information (self):
        print("Name",self.name)

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print("Book Information: ")
        super().print_information()
        print("Author", self.author, f"({self.page_count} pages)")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor


    def print_information(self):
        print("Magazine Information: ")
        super().print_information()
        print("chief editor", self.chief_editor)

publications = []
publications.append(Magazine("Donald Duck", "Aki Hyyppä"))
publications.append(Book("Compartment No.6", "Rosa Liksom",192))

for pubs in publications:
    pubs.print_information()