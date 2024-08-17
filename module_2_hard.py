print('Введите целое число от 3 до 20 : ')
n = int(input())
if 20 > n > 3:
    parol = list()  # Список пар для контроля за повторами
    code = int()
    for i in range(1, n):
        for j in range(2, n):
            k = i + j
            if k <= n and i != j and n % k == 0:  # проверяем условие кратности для текущей пары
                if [j, i] in parol:
                    continue
                else:
                    parol.append([i, j])  # добавляем в список пару удовлетворяющую условиям
                    if i < 10 and j < 10:  # обеспечиваем вывод результата
                        code = code * 100 + i * 10 + j
                    elif i < 10:
                        code = code * 1000 + i * 100 + j
    print('result = ', code)
else:
    print('Введено неправильное число')
