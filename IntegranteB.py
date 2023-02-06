import json

def create_book_json(books):
    with open("books.json", "w") as file:
        json.dump({"books": books}, file)

    print(json.dumps({"books": books}, indent=4))


def read_book_json():
    with open("books.json", "r") as file:
        book_data = json.load(file)

    print(json.dumps(book_data, indent=4))


books = [
    {"title": "Aigues encantades", "cover": "hard", "year": 1908, "pages": 192},
    {"title": "El Quijote", "cover": "soft", "year": 1605, "pages": 994},
    {"title": "El lazarillo de Tormes", "cover": "hard", "year": 1554, "pages": 128},
    {"title": "tirant lo blanc La Odisea", "cover": "soft", "year": 1072, "pages": 1996}
]

create_book_json(books)
read_book_json()
