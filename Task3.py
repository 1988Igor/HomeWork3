#Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from audioop import reverse
from re import X, split
from unicodedata import decimal

lst = [1.1, 1.2, 3.1, 5, 10.01]


temp_str = str(lst)
lst2 = temp_str.replace('10.', '0.').replace('1.', '0.').replace('3.', '0.').replace('5', '0.1').replace('[', '').replace(']','').replace('.','').replace(',','')
print(type(lst2))
lst3 = list(map(int,lst2))
print(type(lst3))




