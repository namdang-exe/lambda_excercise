# Write a Python program to check whether a given string is number or not using Lambda.
x = input("Enter a string: ")

is_num = lambda x: x.replace(".", "").isdigit()

if is_num(x):
    print(f"{x} is a number.")
else:
    print(f"{x} is not a number.")

is_num1 = lambda x: is_num(x[1]) if x[0] == "-" else is_num(x)
if is_num1(x):
    print(f"{x} is a number.")
else:
    print(f"{x} is not a number.")
