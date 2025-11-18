def autoriu_perziura(authors):
    print("\nEsami autoriai:")
    for author in authors:
        print(f"{author['id']}. Vardas pavarde - \"{author['name']}\", Tautybė - \"{author['nationality']}\".")

def autoriaus_pridejimas(authors, id_counter_authors):
    print("Jūs pasirinkote pridėti naują autorių")
    author = input("Įveskite autoriaus vardą ir pavardę: ")
    nationality = input("Įveskite tautybę: ")
    id_counter_authors += 1
    authors.append({'id': id_counter_authors, "name": author, "nationality": nationality})
    return id_counter_authors

def autoriaus_redagavimas(authors):
    edit_id = input("Įveskite autoriaus ID, kurią norite redaguoti: ")
    for i, author in enumerate(authors):
        if str(author['id']) == edit_id:
            authors[i]['name'] = input("Įveskite autoriaus vardą ir pavardę: ")
            authors[i]['nationality'] = input("Įveskite tautybę: ")

def autoriaus_trynimas(authors):
    del_id = input("Įveskite autoriaus ID, kurį norėsite pašalinti: ")
    for author in authors:
        if str(author['id']) == del_id:
            authors.remove(author)
            print(f"Autorius '{author['name']}' sėkmingai pašalintas.")
            break
    else:
        print("Autorius su tokiu ID nerastas.")

def autoriaus_info(authors, library):
    search_id = input("Įveskite autoriaus ID, kurį norite pamatyti: ")
    for author in authors:
        if str(author['id']) == search_id:
            print(f"\nAutorius: {author['name']}, Tautybė: {author['nationality']}")
            knygos = [book for book in library if book['author'] == author['name']]
            if knygos:
                print("Knygos:")
                for book in knygos:
                    print(f"- {book['title']} ({book['year']})")
            else:
                print("Šis autorius neturi įrašytų knygų.")
            break
    else:
        print("Autorius su tokiu ID nerastas.")

def autoriu_meniu(authors, id_counter_authors, library):
    while True:
        print("\n1. Peržiūrėti autorius")
        print("2. Pridėti autorių")
        print("3. Redaguoti autorių")
        print("4. Ištrinti autorių")
        print("5. Peržiūrėti autoriaus info su knygomis")
        print("6. Grįžti į pagrindinį meniu")
        option = input("Pasirinkite: ")
        match option:
            case '1': autoriu_perziura(authors)
            case '2': id_counter_authors = autoriaus_pridejimas(authors, id_counter_authors)
            case '3': autoriaus_redagavimas(authors)
            case '4': autoriaus_trynimas(authors)
            case '5': autoriaus_info(authors, library)
            case '6': break
            case _: print("Pasitikrinkite ką įvedėte")
    return id_counter_authors
