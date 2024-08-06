my_dict = {'Marina': 1987, 'Nikola': 1998, 'Petr': 2005}
print(my_dict)
print('Existing value: ', my_dict['Marina'])
print('Not existing value:', my_dict.get('Georg'))
my_dict.update({'Timofey': 2001, 'Anna': 1989})
Delete_ = my_dict.pop('Petr')
print('Deleted value: ', Delete_)
print('Modified dictionary:', my_dict)
print()# Печать пустой строки
my_set = {'Cat', 2024, (1, 2, 3, 4), 2024, (1, 2, 3, 4)}
print('Set', my_set)
my_set.update([(1, 2), 2023])
my_set.remove(2024)
print('Modified set: ', my_set)
