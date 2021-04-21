print("Thanks for using C/F coverter!")
x = input("How do you want to convert? C-F/F-C:")

if x == ("c-f"):
    c = input("Celsius:")
    print("Fahrenheit:", float(c) * 9 / 5 + 32)

if x == ("C-F"):
    c = input("Celsius:")
    print("Fahrenheit:", float(c) * 9 / 5 + 32)

if x == ("f-c"):
    x = input("Fahrenheit:")
    f = float(x) - 32
    f = f * 5 / 9
    print("Celsius:", f)

if x == ("F-C"):
    x = input("Fahrenheit:")
    f = float(x) - 32
    f = f * 5 / 9
    print("Celsius:", f)