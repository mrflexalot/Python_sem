# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

N = int(input("enter the integer number N: "))
Nproduct = 1
productlist = []
for i in range(1, N+1):
    Nproduct *= i
    productlist.append(Nproduct)
print(f"Your product list of numbers from 1 to {N}: \n {productlist}")
