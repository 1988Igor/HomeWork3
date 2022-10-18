# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def mult_lst(new_lst):
    temp_lst = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
    new_lst = [lst[i]*lst[len(lst)-i-1]for i in range(temp_lst)]
    return new_lst
   
lst = list(map(int, input("Enter the numbers through backspace:\n").split()))
print (f'The product of pairs of numbers in the list is : {mult_lst(lst)}')
