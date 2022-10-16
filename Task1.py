# #Задайте список из нескольких чисел. Напишите программу, 
# # которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

lst = [2, 3, 5, 9, 3,8]
lst2 = []
for i in range(len(lst)):
    lst[i] = int(lst[i])
    if(i) % 2 != 0:
        lst2.append(lst[i])
print(f'On the odd positions we have next elements : {lst2}')
print(f'The summ of elements {lst2} is : {sum(lst2)}')
