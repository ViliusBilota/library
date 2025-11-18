def knygu_perziura(library):
    print("\nEsamos knygos:")
    for item in library:
        print(f"{item['id']}. Autorius - \"{item['author']}\", Pavadinimas - {item['title']}, Metai - {item['year']}.")

def knygos_pridejimas(id_counter_books, library):
    author = input("Įveskite knygos autorių: ")
    title = input("Įveskite knygos pavadinimą: ")
    year = input("Įveskite knygos metus: ")
    id_counter_books += 1
    library.append({'id': id_counter_books, "author": author, "title": title, "year": year})
    return id_counter_books

def knygos_redagavimas(library):
    edit_id = input("Įveskite knygos ID, kurią norite redaguoti: ")
    for i, item in enumerate(library):
        if str(item['id']) == edit_id:
            item['author'] = input("Įveskite knygos autorių: ")
            item['title'] = input("Įveskite knygos pavadinimą: ")
            item['year'] = input("Įveskite knygos metus: ")

def knygos_trynimas(library):
    del_id = input("Įveskite knygos ID, kurį norėsite pašalinti: ")
    for item in library:
        if str(item['id']) == del_id:
            library.remove(item)
            print(f"Knyga '{item['title']}' sėkmingai pašalinta.")
            break
    else:
        print("Knyga su tokiu ID nerasta.")

def knygu_meniu(library, id_counter_books):
    while True:
        print("\n1. Peržiūrėti knygas")
        print("2. Pridėti knygą")
        print("3. Redaguoti knygą")
        print("4. Ištrinti knygą")
        print("5. Grįžti į pagrindinį meniu")
        option = input("Pasirinkite: ")
        match option:
            case '1': knygu_perziura(library)
            case '2': id_counter_books = knygos_pridejimas(id_counter_books, library)
            case '3': knygos_redagavimas(library)
            case '4': knygos_trynimas(library)
            case '5': break
            case _: print("Pasitikrinkite ką įvedėte")
    return id_counter_books
