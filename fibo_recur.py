def fibo_seq(num):
    if num <= 1:
        return num
    else:
        return fibo_seq(num - 1) + fibo_seq(num - 2)


n_term = int(input("Enter n term: "))
if n_term <= 0:
    print("Please enter a positive number")
else:
    for i in range(n_term):
        print(fibo_seq(i))
