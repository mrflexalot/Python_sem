# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

a = int(input("enter the number of quarter: "))
if a == 1:
    print("the coordinates of x vary from 0 to +∞, the coordinates of y vary from 0 to +∞")
elif a == 2:
    print("x vary from -∞ to 0, y vary from 0 to +∞")
elif a == 3:
    print("x vary from -∞ to 0, y vary from -∞ to 0")
elif a == 4:
    print("x vary from 0 to +∞, y vary from -∞ to 0")
else:
    print("invalid number! please, enter the number from 1 to 4")
