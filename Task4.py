#Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input('Enter the number for converting the decimal number to binary: ')) 
b = ''
while n > 0:
    b = str(n % 2) + b
    n = n // 2
 
print(b)
print(type(b))
