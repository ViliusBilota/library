library = [
    {
        'id': 1,
        'author': 'Antanas Škėma',
        'title': 'Balta drobulė',
        'year': 1958
    },
    {
        'id': 2,
        'author': 'Rūta Šepetys',
        'title': 'Tarp pilkų debesų',
        'year': 2011
    },
    {
        'id': 3,
        'author': 'Ernest Hemingway',
        'title': 'Senis ir jūra',
        'year': 1952
    },
    {
        'id': 4,
        'author': 'George Orwell',
        'title': '1984',
        'year': 1949
    },
    {
        'id': 5,
        'author': 'Gabriel García Márquez',
        'title': 'Šimtas metų vienatvės',
        'year': 1967
    }
]

id_counter = 5

while True:
    print("Pasirinkite, ką norite daryti")
    print("1. Peržiūrėti esamas bibliotekos knygas")
    print("2. Pridėti naują knygą")
    print("3. Redaguoti knygą")
    print("4. Ištrinti knygą")
    print("5. Palikti biblioteką")

    option = input()
    match option:
        case '1':
            print("Jūs pasirinkote peržiūrėti esamas bibliotekos knygas")
            for item in library:
                print(item)
        case '2':
            print("Jūs pasirinkote pridėti naują knygą")
            print("Įveskite knygos autorių")
            author = input()
            print("Įveskite knygos pavadinimą")
            title = input()
            print("Įveskite knygos metus")
            year = input()
            id_counter +=1
            item = {'id':id_counter, "Autorius":author, "Pavadinimas":title, "Metai":year}
            library.append(item)
        case '3':
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
        case '4':
            print("Jūs pasirinkote pašalinti knygą")
            print("Įrašykite knygos ID, kurią norėsite šalinti")
            del_id = input()
            for item in library:
                if str(item['id']) == del_id:
                    library.remove(item)
                    break
        case '5':
            print("Jūs pasirinkote palikti biblioteką")
            break
        case _ : #defaultas, kai ivedama belekas
            print("Pasitikrinkite ka ivedete")





