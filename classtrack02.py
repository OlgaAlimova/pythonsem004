# Задайте два числа. Напишите программу, которая найдёт НОК
# (наименьшее общее кратное) этих двух чисел.

a, b = int(input('Введите первое число: ')), int(input('Введите второе число: '))
for s in range(1, a * b + 1):
    if s % a == 0 and s % b == 0:
        print(s)
        break

a, b = int(input('Введите первое число: ')), int(input('Введите второе число: '))

def factorization_number(n):
    indivisibili_list = (2, 3, 5, 7, 9, 11, 13, 17, 19)
    multiple_list = []
    while n > 1:
        for i in indivisibili_list:
            if n % i == 0:
                multiple_list.append(i)
                n = n / i
            else:
                continue
    return(multiple_list)

my_list1 = factorization_number(a)
my_list2 = factorization_number(b)
print(f'my_list1 = {my_list1}')
print(f'my_list2 = {my_list2}')

new_list = []
for k in my_list1:
    for t in my_list2:
        new_list.append(k)
        new_list.append(t)
print(*new_list, sep=' ')

my_set = set(new_list)
print(f'my_set = {my_set}')

smallest = 1
for j in my_set:
    smallest *= j
print(f' наименьшее общее кратное число {a} и {b} = {smallest}')











