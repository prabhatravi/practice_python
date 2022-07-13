car = ("Toyota", "Fortuner", 2021, "White")
print(car)
print(len(car))
print(car[1])
print(car[2:])
car1 = ("Ford", "Raptor", 2019, "Red")
# merging tuples
awesome_cars = car + car1
print(awesome_cars)
# Nested Tuples
awesome_cars1 = (car, car1)
print(awesome_cars1)
# search
cities = ("London", "Paris", "Moscow", "Tokyo")
print("Germany" in cities)
# index
print(cities.index("Paris"))