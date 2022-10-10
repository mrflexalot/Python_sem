# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

N = int(input("enter the number N to make prime factors list for it"))


def Func(n):
    lst = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            lst.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        lst.append(n)
    return lst


print(f"Prime factors list for number N ({N}) -> {Func(N)}")
