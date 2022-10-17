#Напишите программу, которая найдёт c. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# lst = [2, 3, 4, 5, 6]
# print(lst[0::3+1])
# print(lst[0+1::3-1])

def mult_lst(new_lst):
    temp_lst = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
    new_lst = [lst[i]*lst[len(lst)-i-1]for i in range(temp_lst)]
    print (new_lst, end="")


lst = list(map(int, input("Enter the numbers through backspace:\n").split()))
mult_lst(lst)
