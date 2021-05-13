# Write a Python program to square and cube every number in a given list of integers using Lambda.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sq_li = list(map(lambda x: x ** 2, my_list))
print(f"the squares of the list: {sq_li}")

cube_li = list(map(lambda x: x ** 3, my_list))
print(f"the cubes of the list: {cube_li}")
