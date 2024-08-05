immutable_var = 7, 'Вася', False, [3,12]
print('Immutable tuple: ', immutable_var)
# immutable_var[2] = 'Лена'
# выдает ошибку: TypeError: 'tuple' object does not support item assignment
# Поскольку кортеж не поддерживает обращение по элементам
mutable_list = [1,'H',7, 8, 'Вася']
mutable_list [4] = 'Изменяемый'
print('Mutable list: ', mutable_list)
