# # Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# # *Пример:*
# # - Для n = 6: {1: 2, 2: 2.25, 3: 2.37, 4: 2.44, 5: 2.49, 6: 2.52}

# a = int(input("enter the integer number:"))
# sublist = []
# subsum = 0
# for n in range(1, a+1):
#     sublist.append(round(((1+1/n) ** n), 2))
#     subsum += round(((1+1/n) ** n), 2)
# print(f"for number '{a}' subsequence (1+1/n)^n equals: \n{sublist} \nSum of numbers of subsequence is: {subsum}")


#OPTIMIZED VERSION

a = int(input("enter the integer number:"))
lst = [i for i in range(1, a + 1)]
lst_res = [round(((1 + 1/i) ** i), 2) for i in range(1, a + 1)]
print(f"for number '{a}' subsequence (1+1/n)^n equals: \n{dict(zip(lst, lst_res))}")