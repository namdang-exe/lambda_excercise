#  Write a Python program to find if a given string starts with a given character using Lambda.
in_str = input("Enter a string: ")
in_char = input("Enter a letter: ")

# r = lambda x,y: x in y[0]
r = lambda x, y: True if y.startswith(x) else False

print(r(in_char, in_str))
