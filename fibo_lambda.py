import functools
from functools import reduce

# reduce syntax:
# reduce(function, iterable[, initializer])
my_list = [1, 4, 6]
print("The sum of the list is: ")
# print(functools.reduce(lambda a, b: a + b, my_list))

fib_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])

print(fib_series(4))
