#Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
lst = list(map(float, input("Enter the float numbers through backspace:\n").split()))
new_lst = [round(i % 1,2) for i in lst if i%1 != 0]
print(f'The difference between the maximum {max(new_lst)}\
 and minimum value {min(new_lst)} of the elements is: ' , max(new_lst) - min(new_lst))




