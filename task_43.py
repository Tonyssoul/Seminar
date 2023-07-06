# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. 
# Вводится список чисел. Все числа списка находятся на разных строках.


import random
n = int(input('Введите колличество элиментов:'))
lst = [random.randint(-10, 10) for i in range(n)]

cnt = 0
i = 0
while slice := lst[i+1:]:
    per = lst[i]
    cnt += slice.count(per)
    i += 1
print(lst)
print(cnt)

#тоже только проще и в функции
# def func(lst):
# val, *lst = lst # lst = [5, 5, 5, 5, 5] -> val = 5, lst = [5, 5, 5, 5]
# if lst:
# return func(lst) + lst.count(val)

# return 0