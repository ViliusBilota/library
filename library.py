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
            item = {'id':id_counter, "author":author, "title":title, "year":year}
            library.append(item)