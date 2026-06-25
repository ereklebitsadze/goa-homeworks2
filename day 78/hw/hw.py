def sum_all_numbers(*args):
    return sum(args)

# შემოწმება:
print(sum_all_numbers(1, 2, 3))       # დაიბეჭდება: 6
print(sum_all_numbers(10, 20, 30, 40)) # დაიბეჭდება: 100





def print_student_info(**kwargs):
    print("=== სტუდენტის პროფილი ===")
    for key, value in kwargs.items():
        # key.replace('_', ' ').title() ლამაზი ფორმატინგისთვისაა (მაგ: first_name -> First Name)
        print(f"{key.replace('_', ' ').title()}: {value}")
    print("========================")

# შემოწმება:
print_student_info(სახელი="გიორგი", ასაკი=21, ფაკულტეტი="IT", ქალაქი="თბილისი")






class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        print(f"მანქანის ინფორმაცია: {self.brand} {self.model} ({self.year} წელი)")

# შემოწმება:
my_car = Car("Toyota", "Camry", 2022)
my_car.info() # დაიბეჭდება: მანქანის ინფორმაცია: Toyota Camry (2022 წელი)






class Calculator:
    def add(self, *args):
        return sum(args)

# შემოწმება:
my_calc = Calculator()
result = my_calc.add(5, 15, 20, 50)
print(f"ჯამი: {result}") # დაიბეჭდება: ჯამი: 90







class User:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value) # დინამიურად ვქმნით ცვლადებს ობიექტში

    def get_info(self):
        return self.__dict__ # აბრუნებს ობიექტის ყველა თვისებას dictionary-ს სახით

# შემოწმება:
user1 = User(username="gio_99", email="gio@gmail.com", role="Admin")

# შეგვიძლია პირდაპირ ატრიბუტებზეც მივმართოთ:
print(user1.username) # დაიბეჭდება: gio_99

# ან ავიღოთ სრული ინფორმაცია dictionary-ს სახით:
print(user1.get_info()) 
# დაიბეჭდება: {'username': 'gio_99', 'email': 'gio@gmail.com', 'role': 'Admin'}
