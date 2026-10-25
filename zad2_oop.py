
class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (f"Biblioteka w {self.city}, {self.street} {self.zip_code}, "
                f"godziny otwarcia: {self.open_hours}, tel. {self.phone}")

class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date,
                 city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone


    def __str__(self):
        return (f"Pracownik {self.first_name} {self.last_name}, "
                f"zatrudniony: {self.hire_date}, ur.: {self.birth_date}, "
                f"adres: {self.street}, {self.zip_code} {self.city}, "
                f"tel. {self.phone}")




class Book:
    def __init__(self, library, publication_date, author_name,
                 author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (    f"Autor: {self.author_name} {self.author_surname}, "
                    f"wydana: {self.publication_date}, "
                    f"stron: {self.number_of_pages}, "
                    f"biblioteka: {self.library.city}")    

class Student:
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return f"{self.name}"
        


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return (f"Zamówienie z {self.order_date}: "
                f"Student {self.student}, "
                f"obsłużył {self.employee.first_name} {self.employee.last_name}, "
                f"książki: {self.books}")


L1 = Library("Katovice","Cynamonowa","76-777","9:30 - 10:00","543 345 233")
L2 = Library("Wwa","Kreta","12-120","6:00 - 15:00","654 445 667")

b1 = Book(L1,"10.11.2021","Janek","Ancymon",67)
b2 = Book(L2,"10.11.2333","Maciek","Kowalski",543)
b3 = Book(L1,"02.11.2023","Janek","Ananas",99)
b4 = Book(L1, "11.09.2001","Maciek","Banan",2)
b5 = Book(L1,"01.10.1999","Jacek","Nowak",12)

e1 = Employee("Maciek","Nowak","10.10.2000","10.10.1990","Katovicee","Cynamonowa","34-192","777 777 777")
e2 = Employee("Jacek","Kowalskyy","10.10.2000","10.10.1990","Katovicee","Cynamonowa","34-192","777 777 656")
e3 = Employee("Marek","Kaczmarek","12.12.1890","09.09.1872","Warszawa","Wiejska","45-231","676 677 676")

s1 = Student("January")
s2 = Student("Mariusz")

o1 = Order(e1,s1,b1,"12-03-1990")
o2 = Order(e2,s2,b4,"06-05-1766")

print(o1)
print(o2)
