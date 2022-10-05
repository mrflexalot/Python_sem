# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int(input("enter the number k to make fibonacci list for it: "))


def fib(k):
    if k in [1, 2]:
        return 1
    else:
        return fib(k - 1) + fib(k - 2)


fib_lst = [0]
for i in range(1, k + 1):
    fib_lst.append(fib(i))
    fib_lst.insert(0, (fib(i)*(-1)**(i+1)))
print(f"for number {k} fibonacci list is: \n{fib_lst}")
