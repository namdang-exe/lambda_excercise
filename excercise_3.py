my_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# my_list.sort()
# print(my_list)
my_list.sort(key=lambda x: x[1])
print(my_list)
