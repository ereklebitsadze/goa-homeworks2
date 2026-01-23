person = {
    "name": "erekle",
    "age": 15,
    "brand": "Jeep",
    "engine": "2.8L Diesel",
    "available_cars": ["Prius", "Mercedes", "BMW"]
}

item1 = person["name"]
item2 = person["age"]
item3 = person["brand"]
item4 = person["engine"]
item5 = person["available_cars"]

print(item1)
print(item2)
print(item3)
print(item4)
print(item5)

for name in person:
    print(name)