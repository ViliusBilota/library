from data import demo_data
from list_CRUD import*

library = demo_data([])
id_counter = 5

while True:
    print("Sveiki atvykę į biblioteką. Pasirinkite ką norėsite veikti:")
    print("1. Tvarkyti autorius")
    print("2. Tvarkyti knygas")
    print("3. Išeiti")
    option2 = input("Pasirinkite:")
    match option2:
        case '1':
            print("Atidarytas autorių valdymas")
        case '2':
            knygumeniu(library, id_counter)
        case '3':
            print("Pasirinkote išeiti iš bibliotekos")
            break
        case _ :
            print('Pasitikrinkite ką įvedėte')
