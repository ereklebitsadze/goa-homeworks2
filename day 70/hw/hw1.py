# 1. მათემატიკური ოპერატორი
def apply_op(a, b, func):
    return func(a, b)

# გამოყენება:
print(apply_op(3, 4, lambda x, y: x + y))   # 7
print(apply_op(3, 4, lambda x, y: x * y))   # 12


# 2. სალმის გენერატორი
def make_greeter(greeting):
    def greeter(name):
        print(f"{greeting} {name}")
    return greeter

say_hi = make_greeter("გამარჯობა")
say_hi("დავით")   # გამარჯობა დავით


# 3. მარტივი ფილტრი
def my_filter(lst, predicate):
    return [x for x in lst if predicate(x)]

print(my_filter([1, 2, 3, 4, 5], lambda n: n % 2 == 0))  # [2, 4]


# 4. ტექსტის ტრანსფორმაცია
def process_string(text, action):
    return action(text)

print(process_string("Hello World", str.upper))   # HELLO WORLD
print(process_string("Hello World", str.lower))   # hello world
print(process_string("Hello World", lambda s: s[::-1]))  # dlroW olleH


# 5. ფუნქციების სია
def square(x): return x**2
def cube(x): return x**3
def double(x): return x*2

functions = [square, cube, double]
x = 5
for f in functions:
    print(f"{f.__name__}(5) = {f(x)}")


# 6. Logger-ის იმიტაცია
def safe_execute(func, x):
    try:
        func(x)
        print("Success")
    except Exception:
        print("Error")

safe_execute(lambda n: n/0, 5)   # Error
safe_execute(lambda n: n+10, 5)  # Success


# 7. Multiplier Factory
def multiplier(n):
    return lambda x: x * n

double = multiplier(2)
print(double(10))   # 20


# 8. List Mapper
def my_map(func, items):
    return [func(x) for x in items]

print(my_map(lambda n: n*2, [1, 2, 3]))  # [2, 4, 6]


# 9. Conditional Wrapper
def run_if_positive(func, value):
    if value > 0:
        return func(value)
    else:
        return None

print(run_if_positive(lambda n: n*10, 5))   # 50
print(run_if_positive(lambda n: n*10, -3))  # None


# 10. ფუნქციების კომპოზიცია
def compose(f, g):
    return lambda x: f(g(x))

add1 = lambda n: n + 1
square = lambda n: n**2

new_func = compose(square, add1)  # square(add1(x))
print(new_func(4))   # (4+1)^2 = 25
