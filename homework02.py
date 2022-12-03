# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


path_1 = 'polynomial_1.txt'
data = open(path_1, 'r')
for line_1 in data:
    print(line_1)
polinom_1=''.join(line_1)
print(polinom_1)
data.close()

path_2 = 'polynomial_2.txt'
data = open(path_2, 'r')
for line_2 in data:
    print(line_2)
polinom_2=''.join(line_2)
print(polinom_2)
data.close()
print()

def conversionеtonumbers (pol):
    pol_int = []
    num = ''
    for i in pol:
        if i.isdigit():
            num = num + i
        else:
            if num != '':
                pol_int.append(int(num))
                num = ''
    if num != '':
        pol_int.append(int(pol))
    return(pol_int)

def conversionеtodict(pol_int):
    pol_dict = {pol_int[1] : pol_int[0]}
    j = 0
    for j in range(len(pol_int)):
        if j % 2 != 0:
            k = pol_int[j]
            pol_dict[k] = pol_int[j-1]
    pol_dict[1] = pol_int[-1]
    return (pol_dict)

def countpol(pol_int):
    count = 0
    for i in range(len(pol_int)):
        count += 1
    count_pol = count // 2 + 1
    return count_pol


polinom_int_1 = conversionеtonumbers(polinom_1)
# print(f'polinom_int_1 = {polinom_int_1}')
count_pol_1 = countpol(polinom_int_1)
# print(f'count_pol_1 = {count_pol_1}')
polinom_dict_1 = conversionеtodict(polinom_int_1)
print(f'polinom_dict_1 = {polinom_dict_1}')

print()

polinom_int_2 = conversionеtonumbers(polinom_2)
# print(f'polinom_int_2 = {polinom_int_2}')
count_pol_2 = countpol(polinom_int_2)
# print(f'count_pol_2 = {count_pol_2}')
polinom_dict_2 = conversionеtodict(polinom_int_2)
print(f'polinom_dict_2 = {polinom_dict_2}')

print()

for key in polinom_dict_1:
    if polinom_dict_2.get(key, False) == False:
        polinom_dict_2[key] = polinom_dict_1[key]
    else:
        polinom_dict_2[key] += polinom_dict_1[key]
print(f'итоговый словарь = {polinom_dict_2}')

new_polinom = []
for key in polinom_dict_2:
    if key != 1:
        new_polinom.append(f'{polinom_dict_2[key]} * x ** {key} + ')
    else:
        new_polinom.append(f'{polinom_dict_2[key]} * x')
        break
print(*new_polinom)
# new_polinom.pop(-1)

data = open('polynomial_3.txt', 'w')
data.writelines(new_polinom)
data.close()










