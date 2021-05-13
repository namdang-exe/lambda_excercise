# Write a Python program to filter a list of integers using Lambda.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_num_list = list(filter(lambda x: x % 2 == 0, my_list))
print(f"even numbers: {even_num_list}")
odd_num_list = list(filter(lambda x: x % 2 != 0, my_list))
print(f"odd numbers: {odd_num_list}")
