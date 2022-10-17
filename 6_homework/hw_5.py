# # Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# # Пример:
# # - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# lst = [1.1, 1.2, 3.1, 5, 10.01]
# res_lst = [round(i % 1, 2) for i in lst if i % 1 != 0]
# print(f"{lst} => {max(res_lst) - min(res_lst)}")


#OPTIMIZED VERSION (not so optimized btw)
#переделал ввод данных с использованием map.
#list comprehension у меня в решении уже использовался. Понимаю, что не слишком-то и получилось оптимизировать, ну как есть=)


lst = list(map(float, input("Enter the numbers, splitted by space:").split()))
res_lst = [round(i % 1, 2) for i in lst if i % 1 != 0]
print(f"{lst} => {max(res_lst) - min(res_lst)}")
