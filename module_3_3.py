def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()  # работает без аргументов
print_params(b = 25)  # работает с аргументом другого типа
print_params(c = [1,2,3])  # работает с аргументом другого типа

values_list = [1, [1, 2], True]
values_dict = {'a': 1, 'b': 'urban', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
