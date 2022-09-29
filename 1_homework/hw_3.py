# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = float(input("enter the number x, not equal to zero: "))
y = float(input("enter the number y, not equal to zero: "))
if x > 0 and y > 0:
    print("the point is in first quarter")
elif x < 0 and y > 0:
    print("the point is in second quarter")
elif x < 0 and y < 0:
    print("the point is in third quarter")
elif x > 0 and y < 0:
    print("the point is in forth quarter")
else:
    print("the point is on axis or origin")
