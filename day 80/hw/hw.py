# 1. Encapsulation (ინკაპსულაცია):
# ეს არის პრინციპი, როდესაც მონაცემები (ცვლადები) და მათზე სამუშაო მეთოდები (ფუნქციები)
# გაერთიანებულია ერთ მთლიანობაში — კლასში. ის ასევე გულისხმობს შიდა მონაცემების დაცვას
# და გარედან პირდაპირი წვდომის შეზღუდვას (მაგალითად, private ცვლადების გამოყენებით).

# 2. Polymorphism (პოლიმორფიზმი):
# ნიშნავს "მრავალ ფორმას". პროგრამირებაში ეს არის თვისება, როდესაც სხვადასხვა კლასს 
# შეუძლია ჰქონდეს ერთი და იმავე სახელის მქონე მეთოდი (ფუნქცია), მაგრამ თითოეული კლასი 
# ამ მეთოდს თავისებურად, ინდივიდუალურად ასრულებს (მაგალითად, იხ. დავალება 4).

# 3. Instance (ინსტანცია / ობიექტი):
# კლასი არის მხოლოდ ზოგადი შაბლონი (ნახაზი), ხოლო ინსტანცია არის ამ შაბლონის მიხედვით
# მეხსიერებაში შექმნილი კონკრეტული, რეალური ობიექტი თავისი საკუთარი მონაცემებით.





class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        return f"This car is {self.brand} from {self.year}"

# შემოწმება:
my_car = Car("BMW", 2020)
print(my_car.info())  # დაიბეჭდება: This car is BMW from 2020




class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def move(self):
        return "The vehicle is moving"

# Bike კლასი იღებს (მემკვიდრეობითობას გადასცემს) Vehicle კლასს
class Bike(Vehicle):
    # move მეთოდის გადაფარვა (Overriding) სპეციალურად ბაიკისთვის
    def move(self):
        return "The bike is moving fast"

# შემოწმება:
generic_vehicle = Vehicle("Simple Car", 60)
my_bike = Bike("Mountain Bike", 25)

print(generic_vehicle.move()) # დაიბეჭდება: The vehicle is moving
print(my_bike.move())         # დაიბეჭდება: The bike is moving fast





class Bird:
    def move(self):
        return "Flying"

class Fish:
    def move(self):
        return "Swimming"

# ობიექტების (ინსტანციების) შექმნა
pigeon = Bird()
shark = Fish()

# მეთოდების გამოძახება
print(f"Bird is: {pigeon.move()}")  # დაიბეჭდება: Bird is: Flying
print(f"Fish is: {shark.move()}")   # დაიბეჭდება: Fish is: Swimming


# პოლიმორფიზმის სილამაზე იმაშია, რომ შეგვიძლია ციკლში ერთნაირად გამოვიძახოთ ეს მეთოდი:
for animal in [pigeon, shark]:
    print(animal.move())



