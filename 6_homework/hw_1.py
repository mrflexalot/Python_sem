#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# lst = [int(i) for i in input("enter the number sequence to make a unique numbers list").split()]
# lst_res = []
# for i in lst:
#    if lst.count(i) == 1:
#        lst_res.append(i)
# print(f"Unique numbers list for your sequence -> {lst_res}")


#OPTIMIZED VERSION

lst = [int(i) for i in input("enter the number sequence to make a unique numbers list").split()]
print(f"Unique numbers list for your sequence -> {[i for i in lst if lst.count(i) == 1]}")
