# Дано натуральное число N и последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и 
# использовать циклы (даже для ввода и вывода).
# Input: 2 -> 3 4 
# Output: 4 3

import random
def rev(n):
    if n != 0:
        a = str(random.randint(0, 20))
        print(a, end=' ')
        return rev(n-1) + " " + a
    return ' / '

n = int(input('Введите размерность '))
print(rev(n)) 

