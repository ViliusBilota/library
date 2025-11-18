# Library CRUD Project

## Description

This is a simple **Library Management project** created in Python, allowing users to:

* Manage authors (CRUD: create, read, update, delete)
* Manage books (CRUD)
* View all books of a specific author
* Use a simple menu-driven interface for user input

This project was developed **during studies** to demonstrate fundamental Python skills, working with data structures, and modular functions.

---

## Technologies

* Python 3.x
* Data structures: `list`, `dict`
* Functions split into modules (`authors_CRUD.py`, `list_CRUD.py`, `library.py`, `data.py`)

---

## Project Structure

```
library/
│
├── library.py          # Main menu and program execution
├── authors_CRUD.py     # CRUD functions for authors
├── list_CRUD.py        # CRUD functions for books
├── data.py             # Demo data (books and authors)
└── README.md           # This file
```

---

## How to Use

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/library.git
```

2. Navigate to the project folder:

```bash
cd library
```

3. Run the program:

```bash
python library.py
```

4. Choose an action from the menu:

* Manage authors
* Manage books
* Exit the program

---

## Examples

**Viewing authors:**

```
Existing authors:
1. Name - "Antanas Škėma", Nationality - "Lithuanian"
2. Name - "Rūta Šepetys", Nationality - "Lithuanian"
...
```

**Viewing books:**

```
Existing books:
1. Author - "Antanas Škėma", Title - White Shroud, Year - 1958
...
```

---

## Skills Demonstrated

* Working with **Python lists and dictionaries**
* Implementing CRUD logic and user input handling
* Organizing functions and modules
* Basic analytical logic (linking authors to their books)

---

## Notes

* This project is intended to **showcase junior-level skills** in Python.
* Future improvements could include **SQL integration**, persistent data storage, or visualization with Power BI/matplotlib.

---
