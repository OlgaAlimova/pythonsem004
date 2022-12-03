# Задайте строку из набора чисел. Напишите программу,
# которая покажет большее и меньшее число. В качестве
# символа-разделителя используйте пробел.

import random

my_list = []
n = int(input('Введите количество элементов строки: '))
for i in range(n):
    my_list.append(random.randint(1, 100))
print(my_list)

max_el = my_list[0]
for current_el in my_list:
    if current_el > max_el:
        max_el = current_el
print(max_el)

min_el = my_list[0]
for current_el in my_list:
    if current_el < min_el:
        min_el = current_el
print(min_el)

new_list = [max_el, min_el]
print(*new_list, sep=' ')

some_list = input('Введите числа через пробел: ').split(' ')
print(min(some_list))
print(max(some_list))
