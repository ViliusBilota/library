from data import demo_data
from list_CRUD import *
from authors_CRUD import *

books, authors = demo_data()
library = books
id_counter_books = len(books)
id_counter_authors = len(authors)

while True:
    print("\nSveiki atvykę į biblioteką. Pasirinkite veiksmą:")
    print("1. Tvarkyti autorius")
    print("2. Tvarkyti knygas")
    print("3. Išeiti")
    option = input("Pasirinkite: ")
    match option:
        case '1': id_counter_authors = autoriu_meniu(authors, id_counter_authors, library)
        case '2': id_counter_books = knygu_meniu(library, id_counter_books)
        case '3':
            print("Išeinate iš bibliotekos. Iki pasimatymo!")
            break
        case _: print("Pasitikrinkite ką įvedėte")
