# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, 
# у которых два соседних и, при этом, оба соседних элемента меньше данного. 
# Сначала вводится число N — количество элементов в массиве 
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.

import random
n = int(input('Введите колличество элиментов:'))
one = [random.randint(-10, 10) for i in range(n)]
count = 0

for i in range(1, n-1):
    if one[i-1] < one[i] > one[i+1]:
        count += 1

print(one)
print(count)
