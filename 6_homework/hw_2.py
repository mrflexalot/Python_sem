# # Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# # *Пример:*
# # - 6782 -> 23
# # - 0,56 -> 11

# a = input("enter the number to count it's digits sum: ")
# sumnum = 0
# for numberdig in a:
#     if numberdig.isdigit():
#         sumnum += int(numberdig)
# print(f"digits sum in your number {a} is: {sumnum}")


#OPTIMIZED VERSION

a = input("enter the number to count it's digits sum: ")
sumnum = sum([int(numberdig) for numberdig in a if numberdig.isdigit()])
print(sumnum)