# Задача No51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая проверяет, 
# все ли объекты имеют одинаковое значение некоторой характеристики, 
# и возвращают True, если это так. Если значение характеристики для разных объектов отличается - то False. 
# Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это функция, 
# которая принимает объект и вычисляет его характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same if same_by(lambda x: x % 2, values):
# print(‘same’) else:
# print(‘different’)

#1
# def same_by(characteristic, objects):
#     first_characteristic = characteristic(objects[0])
#     return all(characteristic(obj) == first_characteristic for obj in objects)
# values = [0, 2, 10, 6] 
# if same_by(lambda x: x % 2, values):
#     print('same') 
# else:
#     print('different')

#2
# values = [0, 2, 11, 6]
# def same_by(characteristic, objects):
#     s = set([characteristic(x) for x in objects])
#     if len(s) == 1:
#         return True 
#     else:
#         return False

# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')

#3
def same_by(characteristic, objects):
    return len(set(map(characteristic, objects))) < 2
values = [0, 2, 11, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')