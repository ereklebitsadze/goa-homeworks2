print("Welcome to simple calculator")

print("Enter First Number:")
first = input("")

print("Enter Mathematical Symbol(-,+,*,/,//,%):")
thing = input("")

print("Enter Second Number:")
second = input("")

if thing == "+":
    print(int(first) + int(second))

if thing == "-":
    print(int(first) - int(second))

if thing == "*":
    print(int(first) * int(second))

if thing == "/":
    print(int(first) / int(second))

if thing == "//":
    print(int(first) // int(second))

if thing == "%":
    print(int(first) % int(second))

#simple ass calculator