from data import demo_data
from list_CRUD import *
from authors_CRUD import *

books, authors = demo_data([])
id_counter_books = len(books)
id_counter_authors = len(authors)
library = books

while True:
    print("Sveiki atvykę į biblioteką. Pasirinkite ką norėsite veikti:")
    print("1. Tvarkyti autorius")
    print("2. Tvarkyti knygas")
    print("3. Išeiti")
    option2 = input("Pasirinkite:")
    match option2:
        case '1':
            id_counter_authors = autoriu_meniu(authors, id_counter_authors, library)
        case '2':
            id_counter_books = knygumeniu(books, id_counter_books)
        case '3':
            print("Pasirinkote išeiti iš bibliotekos")
            break
        case _ :
            print('Pasitikrinkite ką įvedėte')
