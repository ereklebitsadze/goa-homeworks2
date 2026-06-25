def make_repeater(n):
    def repeater(text):
        return text * n
    return repeater

# გამოყენება:
repeat5 = make_repeater(5)
print(repeat5("გოა "))  # დაიბეჭდება: გოა გოა გოა გოა გოა



def bank_account(initial_balance):
    balance = initial_balance
    
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            print("არასაკმარისი თანხა!")
        else:
            balance -= amount
            print(f"დარჩენილი ნაშთი: {balance}")
        return balance
        
    return withdraw

# გამოყენება:
my_account = bank_account(100)
my_account(20)  # დარჩენილი ნაშთი: 80
my_account(30)  # დარჩენილი ნაშთი: 50



def power_of(base):
    def calculate_power(exponent):
        return base ** exponent
    return calculate_power

# გამოყენება:
base_two = power_of(2)
print(base_two(3))  # დაიბეჭდება: 8



points = 10

def add_point():
    global points  # ამით ვეუბნებით, რომ გლობალური points შეცვალოს
    points += 1 
    print(points)

add_point()  # დაიბეჭდება: 11


def calculate_rectangle_area(a, b):
    return a * b

# დამტკიცება:
# 1. ის არ იყენებს და არ ცვლის არცერთ გლობალურ ცვლადს.
# 2. თუ გადავცემთ 5-ს და 4-ს (calculate_rectangle_area(5, 4)), ის 
#    ყოველთვის დააბრუნებს 20-ს, რამდენიც არ უნდა გამოვიძახოთ.



logs = []

def add_log(message):
    logs.append(message)  # გვერდითი მოვლენა (Side Effect) - ცვლის გლობალურ ცვლადს
    return None

# გამოყენება:
add_log("სისტემა ჩაირთო")
add_log("მომხმარებელი შემოვიდა")
print(logs)  # დაიბეჭდება: ['სისტემა ჩაირთო', 'მომხმარებელი შემოვიდა']



def calculate_tax(tax_rate):
    def apply_to(price):
        return price * tax_rate
    return apply_to

# გამოყენება:
georgian_tax = calculate_tax(0.18)

print(georgian_tax(100))  # დაიბეჭდება: 18.0
print(georgian_tax(250))  # დაიბეჭდება: 45.0




name = "Global"

def test_scopes():
    name = "Local"  # ლოკალური ცვლადი (Shadowing)
    print("ფუნქციის შიგნით:", name)  
    
    # გლობალური ცვლადის დაჭერა ფუნქციის შიგნიდან:
    print("გლობალური მნიშვნელობა შიგნიდან:", globals()['name'])

test_scopes()
print("ფუნქციის გარეთ:", name)




def make_prefix(prefix):
    def add_prefix(name):
        return prefix + name
    return add_prefix

# გამოყენება:
dr_prefix = make_prefix("Dr. ")
print(dr_prefix("Davit"))  # დაიბეჭდება: Dr. Davit



numbers = [1, 5, 8, 10, 15, 20]

# lambda x: x % 5 == 0 ამოწმებს, იყოფა თუ არა რიცხვი 5-ზე უნაშთოდ
divisible_by_5 = list(filter(lambda x: x % 5 == 0, numbers))

print(divisible_by_5)  # დაიბეჭდება: [5, 10, 15, 20]
