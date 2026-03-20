# 1) apply_operation
def apply_operation(numbers, operation):
    return [operation(x) for x in numbers]

print(apply_operation([1, 2, 3], lambda n: n*2))  # [2, 4, 6]


# 2) my_map (როგორც map)
def my_map(func, lst):
    return [func(x) for x in lst]

print(my_map(lambda n: n+1, [1, 2, 3]))  # [2, 3, 4]


# 3) my_filter (როგორც filter)
def my_filter(func, lst):
    return [x for x in lst if func(x)]

print(my_filter(lambda n: n%2==0, [1, 2, 3, 4]))  # [2, 4]


# 4) make_multiplier
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

double = make_multiplier(2)
print(double(10))  # 20


# 5) repeat
def repeat(func, n):
    def wrapper(*args, **kwargs):
        for _ in range(n):
            func(*args, **kwargs)
    return wrapper

def say_hello(name):
    print("Hello", name)

say_hello_3 = repeat(say_hello, 3)
say_hello_3("Erekle")
# Hello Erekle
# Hello Erekle
# Hello Erekle
