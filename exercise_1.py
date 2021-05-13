# Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument
# , also create a lambda function that multiplies argument x with argument y and print the result
add_fifteen = (lambda x: x + 15)
print(add_fifteen(5))

multip = lambda x, y: x * y
print(multip(20, 30))
