import functools
from functools import reduce

my_list = [0, 1, 2, 3]
print("The sum of the list is: ")
# print(functools.reduce(lambda x, _: x + [x[-1] + x[-2]], my_list))

test = lambda x, _: x + [x[-1] + x[-2]]

print(test(my_list, 99))

fibo = lambda n: reduce(test, range(n - 2), [0, 1])
