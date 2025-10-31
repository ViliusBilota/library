def knygu_perziura(library):
    for item in library:
        print(f"{item['id']}. Autorius - \"{item['author']}\", Pavadinimas - {item['title']}, Metai - {item['year']}.")


def pradzia():
    print("Pasirinkite, ką norite daryti")
    print("1. Peržiūrėti esamas bibliotekos knygas")
    print("2. Pridėti naują knygą")
    print("3. Redaguoti knygą")
    print("4. Ištrinti knygą")
    print("5. Palikti biblioteką")

def knygos_pridejimas(id_counter, library):
    print("Jūs pasirinkote pridėti naują knygą")
    print("Įveskite knygos autorių")
    author = input()
    print("Įveskite knygos pavadinimą")
    title = input()
    print("Įveskite knygos metus")
    year = input()
    id_counter += 1
    item = {'id': id_counter, "author": author, "title": title, "year": year}
    library.append(item)
    return id_counter

def knygos_redagavimas(library):
    print("Jūs pasirinkote redaguoti knygą")
    print("Įrašykite knygos ID, kurią norite redaguoti")
    edit_id = input()
    for i, item in enumerate(library):
        if str(item['id']) == edit_id:
            print(item)
            print("Įveskite knygos autorių")
            library[i]['Autorius'] = input()
            print("Įveskite knygos pavadinimą")
            library[i]['Pavadinimas'] = input()
            print("Įveskite knygos metus")
            library[i]['Metai'] = float(input())

def knygos_trynimas(library):
    print("Jūs pasirinkote pašalinti knygą")
    print("Įrašykite knygos ID, kurią norėsite šalinti")
    del_id = input()
    for item in demo_data():
        if str(item['id']) == del_id:
            library.remove(item)
            break