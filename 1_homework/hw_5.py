# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

ax = float(input("enter the x coordinate of number a: "))
ay = float(input("enter the y coordinate of number a: "))
bx = float(input("enter the x coordinate of number b: "))
by = float(input("enter the y coordinate of number b: "))
abdistance = round(((bx - ax) ** 2 + (by - ay) ** 2) ** 0.5, 3)
print("distance between point a and b is:", abdistance)
