def knygu_perziura(library):
    print("\nEsamos knygos:")
    for item in library:
        print(f"{item['id']}. Autorius - \"{item['author']}\", Pavadinimas - {item['title']}, Metai - {item['year']}.")

def knygos_pridejimas(id_counter_books, library):
    print("Jūs pasirinkote pridėti naują knygą")
    print("Įveskite knygos autorių")
    author = input()
    print("Įveskite knygos pavadinimą")
    title = input()
    print("Įveskite knygos metus")
    year = input()
    id_counter_books += 1
    item = {'id': id_counter_books, "author": author, "title": title, "year": year}
    library.append(item)
    return id_counter_books

def knygos_redagavimas(library):
    print("Jūs pasirinkote redaguoti knygą")
    print("Įrašykite knygos ID, kurią norite redaguoti")
    edit_id = input()
    for i, item in enumerate(library):
        if str(item['id']) == edit_id:
            print(item)
            print("Įveskite knygos autorių")
            library[i]['author'] = input()
            print("Įveskite knygos pavadinimą")
            library[i]['title'] = input()
            print("Įveskite knygos metus")
            library[i]['year'] = input()

def knygos_trynimas(library):
    print("Jūs pasirinkote pašalinti knygą")
    print("Įrašykite knygos ID, kurią norėsite šalinti")
    del_id = input()
    for item in library:
        if str(item['id']) == del_id:
            library.remove(item)
            print(f"Knyga '{item['title']}' sėkmingai pašalinta.")
            break
    else:
        print("Knyga su tokiu ID nerasta.")


def bibliotekos_pradzia():
    print("Sveiki atvykę į biblioteką. Pasirinkite ką norėsite veikti:")
    print("1. Tvarkyti autorius")
    print("2.Tvarkyti knygas")
    print("3.Išeiti")

def knygumeniu(library, id_counter_books):
    while True:
        print("Pasirinkote knygas. Metas pasirinkti kitą veiksmą:")
        print("1. Peržiūrėti esamas bibliotekos knygas")
        print("2. Pridėti naują knygą")
        print("3. Redaguoti knygą")
        print("4. Ištrinti knygą")
        print("5. Grįžti į pagrindinį meniu")

        option = input()
        match option:
            case '1':
                print("Jūs pasirinkote peržiūrėti esamas bibliotekos knygas")
                knygu_perziura(library)
            case '2':
                id_counter_books = knygos_pridejimas(id_counter_books, library)
            case '3':
                knygos_redagavimas(library)
            case '4':
                knygos_trynimas(library)
            case '5':
                print("Grįžtate į pagrindinį meniu")
                break
            case _:
                print("Pasitikrinkite ką įvedėte")
    return id_counter_books
