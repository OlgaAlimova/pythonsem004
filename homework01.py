# Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл
# многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или
# x² + 5 = 0 или 10*x² = 0

import random

k = int(input('Введите степень многочлена: '))
n = k
my_list = []
for i in range(k+1):
    while k > 1:
        coefficient_polynomial = random.randint(0, 100)
        my_list.append(f'{coefficient_polynomial} * x ** {k} + ')
        k -= 1
    else:
        my_list.append(f'{coefficient_polynomial} * x')
        break
print(*my_list, sep=' ')

data = open('polynomial_2.txt', 'w')
data.writelines(my_list)
data.close()

