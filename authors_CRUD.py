def autoriu_perziura(authors):
    print("\nEsami autoriai:")
    for author in authors:
        print(f"{author['id']}. Vardas pavarde - \"{author['name']}\", Tautybė - \"{author['nationality']}\".")

def autoriu_meniu(authors, id_counter_authors, library):
    while True:
        print("Pasirinkote autorius. Metas pasirinkti kitą veiksmą:")
        print("1. Peržiūrėti esamus autorius")
        print("2. Pridėti naują autorių")
        print("3. Redaguoti autorių")
        print("4. Ištrinti autorių")
        print("5. Peržiūrėti autoriaus info su jo knygomis")
        print("6. Grįžti į pagrindinį meniu")

        option = input()
        match option:
            case '1':
                print("Jūs pasirinkote peržiūrėti esamus autorius")
                autoriu_perziura(authors)
            case '2':
                id_counter_authors = autoriaus_pridejimas(authors, id_counter_authors)
            case '3':
                autoriaus_redagavimas(authors)
            case '4':
                autoriaus_trynimas(authors)
            case '5':
                autoriaus_info(authors, library)
            case '6':
                print("Grįžtate į pagrindinį meniu")
                break
            case _:
                print("Pasitikrinkite ką įvedėte")
    return id_counter_authors

def autoriaus_pridejimas(authors, id_counter_authors):
    print("Jūs pasirinkote pridėti naują autorių")
    print("Įveskite autoriaus vardą ir pavardę")
    author = input()
    print("Įveskite tautybę")
    nationality = input()
    id_counter_authors += 1
    item = {'id': id_counter_authors, "name": author, "nationality": nationality}
    authors.append(item)
    return id_counter_authors

def autoriaus_redagavimas(authors):
    print("Jūs pasirinkote redaguoti autorių")
    print("Įrašykite autoriaus ID, kurią norite redaguoti")
    edit_id = input()
    for i, author in enumerate(authors):
        if str(author['id']) == edit_id:
            print(author)
            print("Įveskite autorių")
            authors[i]['name'] = input()
            print("Įveskite tautybę")
            authors[i]['nationality'] = input()

def autorius_trynimas(authors):
    print("Jūs pasirinkote pašalinti autorių")
    print("Įrašykite autoriaus ID, kurį norėsite šalinti")
    del_id = input()
    for author in authors:
        if str(author['id']) == del_id:
            authors.remove(author)
            print(f"Autorius '{author['name']}' sėkmingai pašalintas.")
            break
    else:
        print("Autorius su tokiu ID nerastas.")

def autoriaus_info(authors, library):
    print("Autoriaus ID, kurį norite pamatyti:")
    search_id = input()

    for author in authors:
        if str(author['id']) == search_id:
            print(f"\nAutorius: {author['name']}, Tautybė: {author['nationality']}")
            autoriaus_knygos = [book for book in library if book['author'] == author['name']]

            if autoriaus_knygos:
                print("Knygos:")
                for book in autoriaus_knygos:
                    print(f"- {book['title']} ({book['year']})")
            else:
                print("Šis autorius neturi įrašytų knygų.")
            break
    else:
        print("Autorius su tokiu ID nerastas.")