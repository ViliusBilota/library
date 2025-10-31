from data import demo_data
from list_CRUD import*

library = demo_data([])
id_counter = 5


while True:
    pradzia()
    option = input()
    match option:
        case '1':
            print("Jūs pasirinkote peržiūrėti esamas bibliotekos knygas")
            knygu_perziura(library)
        case '2':
            id_counter = knygos_pridejimas(id_counter, library)
        case '3':
            knygos_redagavimas(library)
        case '4':
            knygos_trynimas(library)
        case '5':
            print("Jūs pasirinkote palikti biblioteką")
            break
        case _ :
            print("Pasitikrinkite ką įvedėte")





