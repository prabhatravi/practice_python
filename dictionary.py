empty_dict = {}  # Empty dictionary
print(empty_dict)

phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(phone_book)
# using dict() constructor
phone_book = dict(Batman=468426, Cersei=237734, Ghostbusters=44678)
# Keys will automatically be converted to strings
print(phone_book)

# Alternative approach
phone_book = dict([('Batman', 468426),
                   ('Cersei', 237734),
                   ('Ghostbusters', 44678)])
print(phone_book)
print(phone_book["Cersei"])
print(phone_book.get("Ghostbusters"))

# New entry
phone_book["Godzilla"] = 46394
print(phone_book)

# remove entry
del phone_book["Batman"]
print(phone_book)

# pop() or popitem()
cersei = phone_book.pop("Cersei")
print(phone_book)
print(cersei)

lastAdded = phone_book.popitem()
print(phone_book)
print(lastAdded)

# length of dictionay
print(len(phone_book))

# checking key existence
print("Batman" in phone_book)

# copying the content
second_phone_book = {"Catwoman": 67423, "Jaime": 237734, "Godzilla": 37623}
# Add secondphone_book to phone_book
phone_book.update(second_phone_book)
print(phone_book)

# Dictionary comprehension
houses = {1: "Gryffindor", 2: "Slytherin", 3: "Hufflepuff", 4: "Ravenclaw"}
new_houses = {n**2: house + "!" for (n, house) in houses.items()}
print(houses)
print(new_houses)