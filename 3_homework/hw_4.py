# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# Вариант 1

# a = int(input("enter the decimal number to convert it to binary number: "))
# print(f"{a} -> {bin(a)[2:]}")

# Вариант 2

a = int(input("enter the decimal number to convert it to binary number: "))
b = ''
print(f"{a} ->", end=' ')
while a != 0:
    b = str(a % 2) + b
    a //= 2
print(b)
