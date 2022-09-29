# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

a = int(input("enter the number to check if it's weekend or not: "))
if a == 6:
    print("yes, it's a weekend- saturday")
elif a == 7:
    print("yes, it's a weekend- sunday")
elif a == 5:
    print("no, it's not a weekend - friday")
elif a == 4:
    print("no, it's not a weekend - thursday")
elif a == 3:
    print("no, it's not a weekend - wednesday")
elif a == 2:
    print("no, it's not a weekend - tuesday")
elif a == 1:
    print("no, it's not a weekend - monday")
else:
    print("invalid number")
