# # Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# # Пример:
# # - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# lst = [2, 3, 5, 9, 3]
# res = 0
# for i in range(1, len(lst), 2):
#     res += lst[i]
# print(f"Sum of numbers on not even positions of {lst} list equals: \n{res}")


#OPTIMIZED VERSION

lst = input("Enter the number list to count sum of numbers on odd positions").split()
print(sum([int(lst[i]) for i in range(1, len(lst), 2) if lst[i].isdigit()]))